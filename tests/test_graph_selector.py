from src.graph_selector import GraphSelector


def test_graph_selector_graph_number_1(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: "1")
    assert GraphSelector.graph_selector(store_traces=False) == ("resources/test_graphs/G2-1.txt", "")


def test_graph_selector_graph_with_any_number(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: "12")
    assert GraphSelector.graph_selector(store_traces=False) == ("resources/test_graphs/G2-12.txt", "")
