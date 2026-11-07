
import pytest

from main import prosjecna_cijena


def test_prosjecna_cijena(tmp_path):
    fajl = tmp_path / "rezervacije.csv"
    fajl.write_text(
        "gost,noci,cijena_noci\n"
        "Ana,2,100\n"
        "Marko,3,200\n"
        "Jovana,1,150\n",
        encoding="utf-8"
    )

    assert prosjecna_cijena(fajl) == pytest.approx(158.3333333333)


def test_prazan_csv(tmp_path):
    fajl = tmp_path / "prazan.csv"
    fajl.write_text(
        "gost,noci,cijena_noci\n",
        encoding="utf-8"
    )

    with pytest.raises(ValueError):
        prosjecna_cijena(fajl)


def test_neispravni_podaci(tmp_path):
    fajl = tmp_path / "greska.csv"
    fajl.write_text(
        "gost,noci,cijena_noci\n"
        "Ana,dva,100\n",
        encoding="utf-8"
    )

    with pytest.raises(ValueError):
        prosjecna_cijena(fajl)
