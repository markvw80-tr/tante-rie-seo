#!/bin/zsh
# Wekelijkse migratiemonitor Tante Rie (launchd: nl.tanterie.migratiemonitor)
export PYTHONWARNINGS=ignore
PROJECT="/Users/markvanwijk/Tante Rie SEO"
LOG="$PROJECT/scripts/logs/migratiemonitor.log"
mkdir -p "$PROJECT/scripts/logs"
cd "$PROJECT" || exit 1
echo "=== $(date '+%Y-%m-%d %H:%M') start" >> "$LOG"
/Users/markvanwijk/micromamba/bin/python3 "$PROJECT/scripts/migratiemonitor.py" >> "$LOG" 2>&1
RC=$?
echo "=== $(date '+%Y-%m-%d %H:%M') klaar, exitcode $RC" >> "$LOG"
if [ $RC -eq 0 ]; then
  osascript -e 'display notification "Nieuwe migratiemonitor in marketing/rapporten" with title "Tante Rie SEO"' 2>/dev/null
else
  osascript -e 'display notification "Migratiemonitor mislukt, zie scripts/logs" with title "Tante Rie SEO"' 2>/dev/null
fi
exit $RC
