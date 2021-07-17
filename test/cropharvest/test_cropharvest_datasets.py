from cropharvest.datasets import CropHarvest


def test_combination(monkeypatch, tmpdir) -> None:
    def __init__(self, root, task=None, download=False):
        self.filepaths = ["a", "a", "b", "b", "b"]
        self.y_vals = [1, 1, 0, 0, 0]

    monkeypatch.setattr(CropHarvest, "__init__", __init__)

    cropharvest = CropHarvest(root=tmpdir)

    for seed in range(10):
        cropharvest.shuffle(seed=seed)

        for i in range(len(cropharvest)):
            filepath = cropharvest.filepaths[i]
            if filepath == "a":
                assert cropharvest.y_vals[i] == 1
            else:
                assert cropharvest.y_vals[i] == 0


def test_get_positive_negative_indices(monkeypatch, tmpdir) -> None:
    def __init__(self, root, task=None, download=False):
        self.filepaths = ["a", "a", "b", "b", "b"]
        self.y_vals = [1, 1, 0, 0, 0]

    monkeypatch.setattr(CropHarvest, "__init__", __init__)

    cropharvest = CropHarvest(root=tmpdir)

    pos, neg = cropharvest._get_positive_and_negative_indices()

    assert pos == [0, 1]
    assert neg == [2, 3, 4]