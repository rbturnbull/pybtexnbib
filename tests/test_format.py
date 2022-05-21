from pathlib import Path
from pybtex import format_from_files, format_from_file

marcelis = "[1] Carlo LM Marcelis and Arjan PM de Brouwer. Feingold syndrome 1. In Margaret P Adam, Holly H Ardinger, Roberta A Pagon, Stephanie E Wallace, Lora JH Bean, Karen W Gripp, Ghayda M Mirzaa, and Anne Amemiya, editors, GeneReviews(®). University of Washington, Seattle, 1993.\n"
files_dir = Path(__file__).parent / "files"


def test_format_from_files():
    result = format_from_files(
        [files_dir/"marcelis-20301770.nbib"], 
        style="plain", 
        output_backend="plaintext",
        bib_format="nbib",
    )
    print(result)
    assert result == marcelis


def test_format_from_file():
    result = format_from_file(
        files_dir/"marcelis-20301770.nbib", 
        style="plain", 
        output_backend="plaintext",
        bib_format="nbib",
    )
    assert result == marcelis


def test_format_from_files_suffix():
    result = format_from_files(
        [files_dir/"marcelis-20301770.nbib"], 
        style="plain", 
        output_backend="plaintext",
        bib_format="suffix",
    )
    assert result == marcelis


def test_format_from_file_suffix():
    result = format_from_file(
        files_dir/"marcelis-20301770.nbib", 
        style="plain", 
        output_backend="plaintext",
        bib_format="suffix",
    )
    assert result == marcelis


def test_format_from_files_suffix_multi():
    result = format_from_files(
        [files_dir/"marcelis-20301770.nbib", files_dir/"Knuth1986.bib"], 
        style="plain", 
        output_backend="plaintext",
        bib_format="suffix",
    )
    expected = (
        "[1] Donald E. Knuth. The \TeX  Book. Addison-Wesley Professional, 1986.\n"
        "[2] Carlo LM Marcelis and Arjan PM de Brouwer. Feingold syndrome 1. In Margaret P Adam, Holly H Ardinger, Roberta A Pagon, Stephanie E Wallace, Lora JH Bean, Karen W Gripp, Ghayda M Mirzaa, and Anne Amemiya, editors, GeneReviews(®). University of Washington, Seattle, 1993.\n"
    )
    assert result == expected

