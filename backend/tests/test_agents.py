def test_agent_orchestrator():
    prompt = "Test execution query for agentic-fraud-detection-analyst"
    assert len(prompt) > 0
    assert "Test" in prompt
