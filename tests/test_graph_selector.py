from src.graph_selector import GraphSelector


def test_graph_selector_graph_number_1(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: "1")
    assert GraphSelector.graph_selector(store_traces=False) == ("resources/test_graphs/1.txt", "")


def test_graph_selector_graph_with_any_number(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: "12")
    assert GraphSelector.graph_selector(store_traces=False) == ("resources/test_graphs/12.txt", "")


def test_graph_selector_when_store_traces(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda: "1")
    assert GraphSelector.graph_selector(store_traces=True) == \
           ("resources/test_graphs/1.txt", "resources/execution_traces/trace_1.txt")


def test_graph_selector_with_invalid_input(mocker, capsys):
    mocker.patch('builtins.input', side_effect=["17", "3"])
    GraphSelector.graph_selector(store_traces=True)
    captured = capsys.readouterr()
    assert captured.out == "Entrez le numéro du graphe que vous souhaitez tester : Entrez le numéro du graphe que " \
                           "vous souhaitez tester (Veuillez entrer un nombre entre 1 " \
                           "et 13 inclus) : "
