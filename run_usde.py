#!/usr/bin/env python3
import sys
import os
import json
import time

# Ensure sftoe is importable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sftoe.usde import SmithianUSDE

def print_help():
    print("""
Smithian Fold Theory of Everything — Universal Self-Discovery Engine (USDE)

Usage:
  python3 run_usde.py [options]

Options:
  --sweep          Generate coordinate states and compute binary orbits.
  --closed         Enumerate the closed-set algebra under folds 2,3,5,7.
  --prove          Run the T1-T12 auto-proof matrix on candidate sectors.
  --align          Solve polynomials for proven sectors and match against live PDG.
  --report         Generate a detailed publication-grade scientific Markdown report.
  --ollama MODEL    Generate an LLM inference-driven scientific report using Ollama.
  --daemon         Run autonomously at maximum capacity, incrementing N and exporting results.
  --report-every N Set the number of new alignments required to trigger inference (default: 1).
  --max-denom N    Set the maximum denominator depth (default: 60).
  --help           Show this help message.
""")

def main():
    args = sys.argv[1:]
    if not args or "--help" in args:
        print_help()
        sys.exit(0)

    # Parse max-denom if present
    max_denom = 60
    if "--max-denom" in args:
        try:
            idx = args.index("--max-denom")
            max_denom = int(args[idx + 1])
        except (ValueError, IndexError):
            print("Error: --max-denom requires an integer argument.")
            sys.exit(1)

    usde = SmithianUSDE(max_denom_limit=max_denom)

    if "--sweep" in args:
        print(f"Executing sweep at depth N={max_denom}...")
        closed = usde.closed_set(seed_to=max_denom)
        print(f"Scanned {len(closed)} unique coordinates.")
        # Print a small subset of coordinates
        print("Sample of generated coordinates:")
        sample = sorted(list(closed))[:20]
        print(", ".join(str(x) for x in sample) + " ...")

    elif "--closed" in args:
        print(f"Enumerating closed set for seed depth {max_denom}...")
        closed = usde.closed_set(seed_to=max_denom)
        print(f"Closed-set size: {len(closed)}")
        print("\nCoordinates:")
        line = "   "
        for x in sorted(list(closed)):
            s = str(x) + " "
            if len(line) + len(s) > 100:
                print(line)
                line = "   "
            line += s
        if line.strip():
            print(line)

    elif "--prove" in args:
        print(f"Running T1-T12 proof matrix on candidate sectors up to N={max_denom}...")
        usde.autonomous_loop(console_output=True)

    elif "--align" in args:
        print(f"Running eigenvalue solver and cross-referencing against live PDG databases...")
        res = usde.autonomous_loop(console_output=False)
        print(f"Found {len(res['alignments'])} alignments:")
        for m in res['alignments']:
            print(f"  Sector m={m['sector']} -> Match: {m['name']} (calculated: {m['calculated']:.6f}, measured: {m['measured']:.6f}, dev: {m['deviation_pct']:.4f}%)")

    elif "--report" in args:
        print(f"Generating publication-grade scientific report at depth N={max_denom}...")
        report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "usde_reports", "discovery_atlas.md")
        sectors_num = usde.generate_academic_report(output_path=report_path)
        print(f"Report generated successfully with {sectors_num} sectors explained.")
        print(f"Location: {report_path}")

    elif "--ollama" in args:
        try:
            idx = args.index("--ollama")
            model_name = args[idx + 1]
        except (ValueError, IndexError):
            print("Error: --ollama requires a model name argument (e.g. --ollama gemma4:26b).")
            sys.exit(1)
        print(f"Generating LLM inference-driven scientific report using local Ollama model '{model_name}'...")
        report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "usde_reports", "discovery_atlas_inference.md")
        sectors_num = usde.generate_inference_report(model_name=model_name, output_path=report_path)
        print(f"Report generated successfully with {sectors_num} sectors explained.")
        print(f"Location: {report_path}")

    elif "--daemon" in args:
        reports_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "usde_reports")
        os.makedirs(reports_dir, exist_ok=True)
        log_path = os.path.join(reports_dir, "usde_daemon.log")
        data_path = os.path.join(reports_dir, "usde_discoveries.json")
        
        # Check if Ollama model was provided as part of daemon args
        ollama_model = None
        if "--ollama" in args:
            try:
                idx = args.index("--ollama")
                ollama_model = args[idx + 1]
            except (ValueError, IndexError):
                print("Error: --ollama requires a model name argument.")
                sys.exit(1)
                
        # Check if report-every was provided
        report_every = 1
        if "--report-every" in args:
            try:
                idx = args.index("--report-every")
                report_every = int(args[idx + 1])
            except (ValueError, IndexError):
                print("Error: --report-every requires an integer argument.")
                sys.exit(1)
                
        print(f"USDE running in daemon mode. Logging to reports/usde_daemon.log...")
        if ollama_model:
            print(f"Ollama reporting enabled using model '{ollama_model}'. Output: discovery_atlas_inference.md")
            print(f"Update trigger: every {report_every} new alignments.")
        print("Press Ctrl+C to terminate.")
        
        current_n = 10
        all_alignments = []
        unreported_new_alignments = []
        
        with open(log_path, "w") as log:
            log.write(f"=== USDE Daemon started at {time.strftime('%Y-%m-%d %H:%M:%S')} ===\n")
            if ollama_model:
                log.write(f"Ollama model: {ollama_model}\n")
                log.write(f"Report every: {report_every}\n")
            
        try:
            while True:
                t0 = time.time()
                # Run USDE for current_n
                run_usde = SmithianUSDE(max_denom_limit=current_n)
                res = run_usde.autonomous_loop(console_output=False)
                
                log_line = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] N={current_n:3} | Scanned={res['coordinates_scanned']:5} | Proven={res['sectors_proven']:2} | Alignments={len(res['alignments'])} | Time={time.time()-t0:.2f}s\n"
                print(log_line, end="")
                
                with open(log_path, "a") as log:
                    log.write(log_line)
                    for m in res['alignments']:
                        log.write(f"   -> Alignment: Sector {m['sector']} matches {m['name']} (dev: {m['deviation_pct']:.4f}%)\n")
                
                new_alignments_this_step = False
                for m in res['alignments']:
                    if m not in all_alignments:
                        all_alignments.append(m)
                        unreported_new_alignments.append(m)
                        new_alignments_this_step = True
                        
                if new_alignments_this_step:
                    with open(data_path, "w") as df:
                        json.dump(all_alignments, df, indent=2)
                    
                    # If LLM model is provided and trigger count is reached
                    if ollama_model and len(unreported_new_alignments) >= report_every:
                        log_msg = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Triggering local LLM inference via '{ollama_model}' for {len(unreported_new_alignments)} new discoveries...\n"
                        print(log_msg, end="")
                        with open(log_path, "a") as log:
                            log.write(log_msg)
                            
                        # Retry loop for LLM report generation (up to 3 times) to avoid crash/truncation
                        for attempt in range(1, 4):
                            try:
                                report_path = os.path.join(reports_dir, "discovery_atlas_inference.md")
                                run_usde.generate_inference_report(model_name=ollama_model, output_path=report_path, limit_to_matches=True)
                                log_success = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] LLM inference report updated successfully.\n"
                                print(log_success, end="")
                                with open(log_path, "a") as log:
                                    log.write(log_success)
                                unreported_new_alignments = []
                                break
                            except Exception as ex:
                                err_msg = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] LLM report generation attempt {attempt} failed: {ex}\n"
                                print(err_msg, end="")
                                with open(log_path, "a") as log:
                                    log.write(err_msg)
                                if attempt < 3:
                                    time.sleep(2)
                                    
                current_n += 5
                # Brief sleep to allow cancellation
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nUSDE Daemon stopped by user.")

if __name__ == "__main__":
    main()
