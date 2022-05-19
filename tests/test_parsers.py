from unittest import TestCase
from itertools import zip_longest
from pybtex.database import BibliographyData, Entry, Person
from pybtex.utils import OrderedCaseInsensitiveDict
from pybtexnbib import NBIBParser
from pathlib import Path

files_dir = Path(__file__).parent / "files"


class _TestParser(NBIBParser):
    def __init__(self, *args, **kwargs):
        super(_TestParser, self).__init__(*args, **kwargs)
        self.errors = []

    def handle_error(self, error):
        self.errors.append(error)


marcelis = BibliographyData(
  entries=OrderedCaseInsensitiveDict([
    ('Marcelis', Entry('incollection',
      fields=[
        ('type', 'Review; Book Chapter'), 
        ('title', 'Feingold Syndrome 1.'), 
        ('booktitle', 'GeneReviews(®)'), 
        ('publisher', 'University of Washington, Seattle'), 
        ('keywords', 'Oculodigitoesophagoduodenal Syndrome | ODED Syndrome | Oculodigitoesophagoduodenal Syndrome | ODED Syndrome | N-myc proto-oncogene protein | MYCN | Feingold Syndrome 1'), 
        ('date', '1993'), 
        ('abstract', 'CLINICAL CHARACTERISTICS: Feingold syndrome 1 (referred to as FS1 in thisGeneReview) is characterized by digital anomalies (shortening of the 2nd and 5thmiddle phalanx of the hand, clinodactyly of the 5th finger, syndactyly of toes2-3 and/or 4-5, thumb hypoplasia), microcephaly, facial dysmorphism (shortpalpebral fissures and micrognathia), gastrointestinal atresias (primarilyesophageal and/or duodenal), and mild-to-moderate learning disability.DIAGNOSIS/TESTING: The diagnosis of FS1 is established in a proband withsuggestive clinical findings and a heterozygous pathogenic variant in MYCNidentified by molecular genetic testing. MANAGEMENT: Treatment of manifestations:Gastrointestinal atresia is treated surgically. Mild-to-moderate learningdisabilities are treated in the usual manner. GENETIC COUNSELING: FS1 isinherited in an autosomal dominant manner. Approximately 60% of individuals withFeingold syndrome 1 have an affected parent; the proportion of FS1 caused by a denovo MYCN pathogenic variant is unknown. Each child of an individual with FS1 hasa 50% chance of inheriting the MYCN pathogenic variant. When the MYCN pathogenicvariant has been identified in an affected family member, prenatal andpreimplantation genetic testing are possible.'), 
        ('PMID', '20301770'), 
        ('STAT', 'Publisher'), 
        ('DRDT', '20190404'), 
        ('CTDT', '20090630'), 
        ('CI', 'Copyright © 1993-2022, University of Washington, Seattle. GeneReviews is aregistered trademark of the University of Washington, Seattle. All rightsreserved.'), ('ED', 'Adam MP; Ardinger HH; Pagon RA; Wallace SE; Bean LJH; Gripp KW; Mirzaa GM; Amemiya A'), 
        ('AU', 'Marcelis CLM; de Brouwer APM'), 
        ('AD', 'Department of Human Genetics, Radboud University Nijmegen Medical Center,Nijmegen, The Netherlands; Assistant Professor, Department of Human Genetics, Radboud University NijmegenMedical Center, Nijmegen, The Netherlands'), 
        ('LA', 'eng'), 
        ('PL', 'Seattle (WA)'), 
        ('OTO', 'NLM'), 
        ('EDAT', '2019/04/04 00:00'), 
        ('CRDT', '2019/04/04 00:00'), 
        ('AID', 'NBK7050 [bookaccession]')],
      persons=OrderedCaseInsensitiveDict([('author', [Person('Marcelis, Carlo LM'), Person('de Brouwer, Arjan PM')]), ('editor', [Person('Adam, Margaret P'), Person('Ardinger, Holly H'), Person('Pagon, Roberta A'), Person('Wallace, Stephanie E'), Person('Bean, Lora JH'), Person('Gripp, Karen W'), Person('Mirzaa, Ghayda M'), Person('Amemiya, Anne')])])))]),

  preamble=[])


class ParserTest(object):
    input_string = None
    input_strings = []
    correct_result = None
    parser_options = {}
    errors = []

    def setUp(self):
        if not self.input_strings:
            self.input_strings = [self.input_string]

    def test_parser(self):
        parser = _TestParser(encoding="UTF-8", **self.parser_options)
        for input_string in self.input_strings:
            parser.parse_string(input_string)
        result = parser.data
        correct_result = self.correct_result

        print("Expected result:")
        print(correct_result)
        print("Parsed result:")
        print(result)
        assert (
            result == correct_result
        ), f"Parsed result:\n--------\n{result}\n--------\nis not the same as expected:\n--------\n{correct_result}"
        for error, correct_error in zip_longest(parser.errors, self.errors):
            actual_error = str(error)
            assert actual_error == correct_error


class EmptyDataTest(ParserTest, TestCase):
    input_string = ""
    correct_result = BibliographyData()


class TestSingleJournal(ParserTest, TestCase):
    input_string = """
        PMID- 35503723
        OWN - NLM
        STAT- MEDLINE
        DCOM- 20220505
        LR  - 20220505
        IS  - 2057-5858 (Electronic)
        IS  - 2057-5858 (Linking)
        VI  - 8
        IP  - 5
        DP  - 2022 May
        TI  - Whokaryote: distinguishing eukaryotic and prokaryotic contigs in metagenomes 
            based on gene structure.
        LID - 10.1099/mgen.0.000823 [doi]
        AB  - Metagenomics has become a prominent technology to study the functional potential 
            of all organisms in a microbial community. Most studies focus on the bacterial 
            content of these communities, while ignoring eukaryotic microbes. Indeed, many 
            metagenomics analysis pipelines silently assume that all contigs in a metagenome 
            are prokaryotic, likely resulting in less accurate annotation of eukaryotes in 
            metagenomes. Early detection of eukaryotic contigs allows for eukaryote-specific 
            gene prediction and functional annotation. Here, we developed a classifier that 
            distinguishes eukaryotic from prokaryotic contigs based on foundational 
            differences between these taxa in terms of gene structure. We first developed 
            Whokaryote, a random forest classifier that uses intergenic distance, gene 
            density and gene length as the most important features. We show that, with an 
            estimated recall, precision and accuracy of 94, 96 and 95 %, respectively, this 
            classifier with features grounded in biology can perform almost as well as the 
            classifiers EukRep and Tiara, which use k-mer frequencies as features. By 
            retraining our classifier with Tiara predictions as an additional feature, the 
            weaknesses of both types of classifiers are compensated; the result is 
            Whokaryote+Tiara, an enhanced classifier that outperforms all individual 
            classifiers, with an F1 score of 0.99 for both eukaryotes and prokaryotes, while 
            still being fast. In a reanalysis of metagenome data from a disease-suppressive 
            plant endospheric microbial community, we show how using Whokaryote+Tiara to 
            select contigs for eukaryotic gene prediction facilitates the discovery of 
            several biosynthetic gene clusters that were missed in the original study. 
            Whokaryote (+Tiara) is wrapped in an easily installable package and is freely 
            available from https://github.com/LottePronk/whokaryote.
        FAU - Pronk, Lotte J U
        AU  - Pronk LJU
        AD  - Bioinformatics Group, Wageningen University, Wageningen, The Netherlands.
        FAU - Medema, Marnix H
        AU  - Medema MH
        AD  - Bioinformatics Group, Wageningen University, Wageningen, The Netherlands.
        LA  - eng
        PT  - Journal Article
        PL  - England
        TA  - Microb Genom
        JT  - Microbial genomics
        JID - 101671820
        SB  - IM
        MH  - Bacteria/genetics
        MH  - Eukaryota/genetics
        MH  - *Metagenome
        MH  - Metagenomics/methods
        MH  - *Microbiota/genetics
        OTO - NOTNLM
        OT  - biosynthetic gene cluster
        OT  - gene structure
        OT  - machine learning
        OT  - metagenomics
        OT  - taxonomy
        EDAT- 2022/05/04 06:00
        MHDA- 2022/05/06 06:00
        CRDT- 2022/05/03 13:00
        PHST- 2022/05/03 13:00 [entrez]
        PHST- 2022/05/04 06:00 [pubmed]
        PHST- 2022/05/06 06:00 [medline]
        AID - 10.1099/mgen.0.000823 [doi]
        PST - ppublish
        SO  - Microb Genom. 2022 May;8(5). doi: 10.1099/mgen.0.000823.
    """  
    correct_result = BibliographyData(
  entries=OrderedCaseInsensitiveDict([
    ('Pronk', Entry('article',
      fields=[
        ('type', 'Journal Article'), 
        ('title', 'Whokaryote: distinguishing eukaryotic and prokaryotic contigs in metagenomesbased on gene structure.'), 
        ('date', '2022 May'), 
        ('volume', '8'), 
        ('keywords', 'biosynthetic gene cluster | gene structure | machine learning | metagenomics | taxonomy'), 
        ('issn', '2057-5858 (Electronic); 2057-5858 (Linking)'), 
        ('abstract', 'Metagenomics has become a prominent technology to study the functional potentialof all organisms in a microbial community. Most studies focus on the bacterialcontent of these communities, while ignoring eukaryotic microbes. Indeed, manymetagenomics analysis pipelines silently assume that all contigs in a metagenomeare prokaryotic, likely resulting in less accurate annotation of eukaryotes inmetagenomes. Early detection of eukaryotic contigs allows for eukaryote-specificgene prediction and functional annotation. Here, we developed a classifier thatdistinguishes eukaryotic from prokaryotic contigs based on foundationaldifferences between these taxa in terms of gene structure. We first developedWhokaryote, a random forest classifier that uses intergenic distance, genedensity and gene length as the most important features. We show that, with anestimated recall, precision and accuracy of 94, 96 and 95\u200a%, respectively, thisclassifier with features grounded in biology can perform almost as well as theclassifiers EukRep and Tiara, which use k-mer frequencies as features. Byretraining our classifier with Tiara predictions as an additional feature, theweaknesses of both types of classifiers are compensated; the result isWhokaryote+Tiara, an enhanced classifier that outperforms all individualclassifiers, with an F1 score of 0.99 for both eukaryotes and prokaryotes, whilestill being fast. In a reanalysis of metagenome data from a disease-suppressiveplant endospheric microbial community, we show how using Whokaryote+Tiara\u2009toselect contigs for eukaryotic gene prediction facilitates the discovery ofseveral biosynthetic gene clusters that were missed in the original study.Whokaryote (+Tiara) is wrapped in an easily installable package and is freelyavailable from https://github.com/LottePronk/whokaryote.'), 
        ('doi', '10.1099/mgen.0.000823'), 
        ('PMID', '35503723'), 
        ('OWN', 'NLM'), 
        (
        'STAT', 'MEDLINE'), 
        ('DCOM', '20220505'), 
        ('LR', '20220505'), 
        ('IP', '5'), 
        ('LID', '10.1099/mgen.0.000823 [doi]'), 
        ('AU', 'Pronk LJU; Medema MH'), 
        ('AD', 'Bioinformatics Group, Wageningen University, Wageningen, The Netherlands.; Bioinformatics Group, Wageningen University, Wageningen, The Netherlands.'), 
        ('LA', 'eng'), 
        ('PL', 'England'), ('TA', 'Microb Genom'), 
        ('JT', 'Microbial genomics'), 
        ('JID', '101671820'), 
        ('SB', 'IM'), ('MH', 'Bacteria/genetics; Eukaryota/genetics; *Metagenome; Metagenomics/methods; *Microbiota/genetics'), 
        ('OTO', 'NOTNLM'), 
        ('EDAT', '2022/05/04 06:00'), 
        ('MHDA', '2022/05/06 06:00'), 
        ('CRDT', '2022/05/03 13:00'), 
        ('PHST', '2022/05/03 13:00 [entrez]; 2022/05/04 06:00 [pubmed]; 2022/05/06 06:00 [medline]'), 
        ('PST', 'ppublish'), 
        ('SO', 'Microb Genom. 2022 May;8(5). doi: 10.1099/mgen.0.000823.')],
      persons=OrderedCaseInsensitiveDict([('author', [Person('Pronk, Lotte J U'), Person('Medema, Marnix H')])])))]),

  preamble=[])


class TestSingleBookChapter(ParserTest, TestCase):
    input_string = """
        PMID- 20301770
        STAT- Publisher
        DRDT- 20190404
        CTDT- 20090630
        PB  - University of Washington, Seattle
        DP  - 1993
        TI  - Feingold Syndrome 1.
        BTI - GeneReviews(®)
        AB  - CLINICAL CHARACTERISTICS: Feingold syndrome 1 (referred to as FS1 in this 
            GeneReview) is characterized by digital anomalies (shortening of the 2nd and 5th 
            middle phalanx of the hand, clinodactyly of the 5th finger, syndactyly of toes 
            2-3 and/or 4-5, thumb hypoplasia), microcephaly, facial dysmorphism (short 
            palpebral fissures and micrognathia), gastrointestinal atresias (primarily 
            esophageal and/or duodenal), and mild-to-moderate learning disability. 
            DIAGNOSIS/TESTING: The diagnosis of FS1 is established in a proband with 
            suggestive clinical findings and a heterozygous pathogenic variant in MYCN 
            identified by molecular genetic testing. MANAGEMENT: Treatment of manifestations: 
            Gastrointestinal atresia is treated surgically. Mild-to-moderate learning 
            disabilities are treated in the usual manner. GENETIC COUNSELING: FS1 is 
            inherited in an autosomal dominant manner. Approximately 60% of individuals with 
            Feingold syndrome 1 have an affected parent; the proportion of FS1 caused by a de 
            novo MYCN pathogenic variant is unknown. Each child of an individual with FS1 has 
            a 50% chance of inheriting the MYCN pathogenic variant. When the MYCN pathogenic 
            variant has been identified in an affected family member, prenatal and 
            preimplantation genetic testing are possible.
        CI  - Copyright © 1993-2022, University of Washington, Seattle. GeneReviews is a 
            registered trademark of the University of Washington, Seattle. All rights 
            reserved.
        FED - Adam, Margaret P
        ED  - Adam MP
        FED - Ardinger, Holly H
        ED  - Ardinger HH
        FED - Pagon, Roberta A
        ED  - Pagon RA
        FED - Wallace, Stephanie E
        ED  - Wallace SE
        FED - Bean, Lora JH
        ED  - Bean LJH
        FED - Gripp, Karen W
        ED  - Gripp KW
        FED - Mirzaa, Ghayda M
        ED  - Mirzaa GM
        FED - Amemiya, Anne
        ED  - Amemiya A
        FAU - Marcelis, Carlo LM
        AU  - Marcelis CLM
        AD  - Department of Human Genetics, Radboud University Nijmegen Medical Center, 
            Nijmegen, The Netherlands
        FAU - de Brouwer, Arjan PM
        AU  - de Brouwer APM
        AD  - Assistant Professor, Department of Human Genetics, Radboud University Nijmegen 
            Medical Center, Nijmegen, The Netherlands
        LA  - eng
        PT  - Review
        PT  - Book Chapter
        PL  - Seattle (WA)
        OTO - NLM
        OT  - Oculodigitoesophagoduodenal Syndrome
        OT  - ODED Syndrome
        OT  - Oculodigitoesophagoduodenal Syndrome
        OT  - ODED Syndrome
        OT  - N-myc proto-oncogene protein
        OT  - MYCN
        OT  - Feingold Syndrome 1
        EDAT- 2019/04/04 00:00
        CRDT- 2019/04/04 00:00
        AID - NBK7050 [bookaccession]
    """  
    correct_result = marcelis


def test_parse_file():
    parser = _TestParser()
    parser.parse_file(files_dir / "marcelis-20301770.nbib")
    result = parser.data
    assert result == marcelis
