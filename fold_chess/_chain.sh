#!/bin/bash
cd /Users/mettamazza/Desktop/SFTOM/fold_chess
while pgrep -f _frag_auc_run >/dev/null; do sleep 30; done
python3 -u _growth_fair4.py > /tmp/growth4.log 2>&1
python3 -u fold_query_recovery.py > /tmp/qrec5.log 2>&1
