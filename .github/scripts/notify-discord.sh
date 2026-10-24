#!/bin/sh
set -eu

if [ -z "${DISCORD_WEBHOOK_URL:-}" ]; then
    echo "::warning::DISCORD_WEBHOOK_URL is not configured."
    exit 0
fi

content="[$GITHUB_REPOSITORY] $GITHUB_WORKFLOW: $WORKFLOW_STATUS
$GITHUB_SERVER_URL/$GITHUB_REPOSITORY/actions/runs/$GITHUB_RUN_ID"

jq -n --arg content "$content" '{content: $content, allowed_mentions: {parse: []}}' |
    curl --fail --silent --show-error --connect-timeout 10 --max-time 30 \
        -H 'Content-Type: application/json' --data-binary @- "${DISCORD_WEBHOOK_URL%/github}"
