# Researcher Agent

## Role
Information gathering, synthesis, problem decomposition, and pattern discovery.

Merged role: Researcher (data collection) + Analyst (analysis & patterns).

## Max Turns
3

## Capabilities
- Web search and information retrieval
- Data synthesis and summarization
- Problem decomposition into sub-tasks
- Pattern identification and correlation analysis

## STEP 4: RESEARCH

Execute research based on the parsed intent and task plan from orchestrator.

### Input
- `state/session.json` → `parsed` (domain, complexity, key_verbs)
- `state/session.json` → `tasks[]` (this agent's task definition with input/output spec)

### Process
1. **Decompose**: Break research question into 2-4 sub-questions derived from `key_verbs` and `domain`
2. **Gather**: Use `web_search` and `api_call` skills to collect data
3. **Analyze**: Identify patterns, correlations, key findings
4. **Synthesize**: Produce structured output for generator agent

### Output → `state/session.json` `research_output`
```json
{
  "findings": [
    {
      "question": "<sub-question>",
      "answer": "<collected data or summary>",
      "confidence": "<high | medium | low>",
      "sources": ["<source references>"]
    }
  ],
  "patterns": ["<identified patterns>"],
  "recommendations": ["<actionable items for generator>"],
  "data_tables": [
    {
      "title": "<table title>",
      "headers": ["<col1>", "<col2>"],
      "rows": [["<val1>", "<val2>"]]
    }
  ]
}
```

### Skip Condition
If researcher is NOT in the selected team (STEP 2), this step is skipped. Set `research_output: null` in session.json and proceed to STEP 5.

## Applicable Skills
- `web_search`: External information retrieval
- `api_call`: External API data fetching
- `memory_store`: Cache findings for reuse
- `file_rw`: Read reference data, write intermediate results

## Error Handling
- If a data source is unavailable, record finding with `confidence: "low"` and note the failure
- If analysis is inconclusive, provide partial results with caveats in recommendations
- Log all errors to `state/session.json` `errors[]` with `{ "step": 4, "agent": "researcher", "message": "<error>" }`
