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
    entries=OrderedCaseInsensitiveDict(
        [
            (
                'Marcelis',
                Entry(
                    'incollection',
                    fields=[
                        ('type', 'Review; Book Chapter'),
                        ('title', 'Feingold Syndrome 1.'),
                        ('booktitle', 'GeneReviews(®)'),
                        ('publisher', 'University of Washington, Seattle'),
                        (
                            'keywords',
                            'Oculodigitoesophagoduodenal Syndrome | ODED Syndrome | Oculodigitoesophagoduodenal Syndrome | ODED Syndrome | N-myc proto-oncogene protein | MYCN | Feingold Syndrome 1',
                        ),
                        ('date', '1993'),
                        (
                            'abstract',
                            'CLINICAL CHARACTERISTICS: Feingold syndrome 1 (referred to as FS1 in thisGeneReview) is characterized by digital anomalies (shortening of the 2nd and 5thmiddle phalanx of the hand, clinodactyly of the 5th finger, syndactyly of toes2-3 and/or 4-5, thumb hypoplasia), microcephaly, facial dysmorphism (shortpalpebral fissures and micrognathia), gastrointestinal atresias (primarilyesophageal and/or duodenal), and mild-to-moderate learning disability.DIAGNOSIS/TESTING: The diagnosis of FS1 is established in a proband withsuggestive clinical findings and a heterozygous pathogenic variant in MYCNidentified by molecular genetic testing. MANAGEMENT: Treatment of manifestations:Gastrointestinal atresia is treated surgically. Mild-to-moderate learningdisabilities are treated in the usual manner. GENETIC COUNSELING: FS1 isinherited in an autosomal dominant manner. Approximately 60% of individuals withFeingold syndrome 1 have an affected parent; the proportion of FS1 caused by a denovo MYCN pathogenic variant is unknown. Each child of an individual with FS1 hasa 50% chance of inheriting the MYCN pathogenic variant. When the MYCN pathogenicvariant has been identified in an affected family member, prenatal andpreimplantation genetic testing are possible.',
                        ),
                        ('PMID', '20301770'),
                        ('STAT', 'Publisher'),
                        ('DRDT', '20190404'),
                        ('CTDT', '20090630'),
                        (
                            'CI',
                            'Copyright © 1993-2022, University of Washington, Seattle. GeneReviews is aregistered trademark of the University of Washington, Seattle. All rightsreserved.',
                        ),
                        ('ED', 'Adam MP; Ardinger HH; Pagon RA; Wallace SE; Bean LJH; Gripp KW; Mirzaa GM; Amemiya A'),
                        ('AU', 'Marcelis CLM; de Brouwer APM'),
                        (
                            'AD',
                            'Department of Human Genetics, Radboud University Nijmegen Medical Center,Nijmegen, The Netherlands; Assistant Professor, Department of Human Genetics, Radboud University NijmegenMedical Center, Nijmegen, The Netherlands',
                        ),
                        ('LA', 'eng'),
                        ('PL', 'Seattle (WA)'),
                        ('OTO', 'NLM'),
                        ('EDAT', '2019/04/04 00:00'),
                        ('CRDT', '2019/04/04 00:00'),
                        ('AID', 'NBK7050 [bookaccession]'),
                    ],
                    persons=OrderedCaseInsensitiveDict(
                        [
                            ('author', [Person('Marcelis, Carlo LM'), Person('de Brouwer, Arjan PM')]),
                            (
                                'editor',
                                [
                                    Person('Adam, Margaret P'),
                                    Person('Ardinger, Holly H'),
                                    Person('Pagon, Roberta A'),
                                    Person('Wallace, Stephanie E'),
                                    Person('Bean, Lora JH'),
                                    Person('Gripp, Karen W'),
                                    Person('Mirzaa, Ghayda M'),
                                    Person('Amemiya, Anne'),
                                ],
                            ),
                        ]
                    ),
                ),
            )
        ]
    ),
    preamble=[],
)


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


class TestMarcelis(ParserTest, TestCase):
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
        entries=OrderedCaseInsensitiveDict(
            [
                (
                    'Pronk2022',
                    Entry(
                        'article',
                        fields=[
                            ('type', 'Journal Article'),
                            (
                                'title',
                                'Whokaryote: distinguishing eukaryotic and prokaryotic contigs in metagenomesbased on gene structure.',
                            ),
                            ('journal', 'Microbial genomics'),
                            ('date', '2022 May'),
                            ('volume', '8'),
                            (
                                'keywords',
                                'biosynthetic gene cluster | gene structure | machine learning | metagenomics | taxonomy',
                            ),
                            ('issn', '2057-5858 (Electronic); 2057-5858 (Linking)'),
                            (
                                'abstract',
                                'Metagenomics has become a prominent technology to study the functional potentialof all organisms in a microbial community. Most studies focus on the bacterialcontent of these communities, while ignoring eukaryotic microbes. Indeed, manymetagenomics analysis pipelines silently assume that all contigs in a metagenomeare prokaryotic, likely resulting in less accurate annotation of eukaryotes inmetagenomes. Early detection of eukaryotic contigs allows for eukaryote-specificgene prediction and functional annotation. Here, we developed a classifier thatdistinguishes eukaryotic from prokaryotic contigs based on foundationaldifferences between these taxa in terms of gene structure. We first developedWhokaryote, a random forest classifier that uses intergenic distance, genedensity and gene length as the most important features. We show that, with anestimated recall, precision and accuracy of 94, 96 and 95\u200a%, respectively, thisclassifier with features grounded in biology can perform almost as well as theclassifiers EukRep and Tiara, which use k-mer frequencies as features. Byretraining our classifier with Tiara predictions as an additional feature, theweaknesses of both types of classifiers are compensated; the result isWhokaryote+Tiara, an enhanced classifier that outperforms all individualclassifiers, with an F1 score of 0.99 for both eukaryotes and prokaryotes, whilestill being fast. In a reanalysis of metagenome data from a disease-suppressiveplant endospheric microbial community, we show how using Whokaryote+Tiara\u2009toselect contigs for eukaryotic gene prediction facilitates the discovery ofseveral biosynthetic gene clusters that were missed in the original study.Whokaryote (+Tiara) is wrapped in an easily installable package and is freelyavailable from https://github.com/LottePronk/whokaryote.',
                            ),
                            ('year', '2022'),
                            ('doi', '10.1099/mgen.0.000823'),
                            ('PMID', '35503723'),
                            ('OWN', 'NLM'),
                            ('STAT', 'MEDLINE'),
                            ('DCOM', '20220505'),
                            ('LR', '20220505'),
                            ('IP', '5'),
                            ('LID', '10.1099/mgen.0.000823 [doi]'),
                            ('AU', 'Pronk LJU; Medema MH'),
                            (
                                'AD',
                                'Bioinformatics Group, Wageningen University, Wageningen, The Netherlands.; Bioinformatics Group, Wageningen University, Wageningen, The Netherlands.',
                            ),
                            ('LA', 'eng'),
                            ('PL', 'England'),
                            ('TA', 'Microb Genom'),
                            ('JID', '101671820'),
                            ('SB', 'IM'),
                            (
                                'MH',
                                'Bacteria/genetics; Eukaryota/genetics; *Metagenome; Metagenomics/methods; *Microbiota/genetics',
                            ),
                            ('OTO', 'NOTNLM'),
                            ('EDAT', '2022/05/04 06:00'),
                            ('MHDA', '2022/05/06 06:00'),
                            ('CRDT', '2022/05/03 13:00'),
                            (
                                'PHST',
                                '2022/05/03 13:00 [entrez]; 2022/05/04 06:00 [pubmed]; 2022/05/06 06:00 [medline]',
                            ),
                            ('PST', 'ppublish'),
                            ('SO', 'Microb Genom. 2022 May;8(5). doi: 10.1099/mgen.0.000823.'),
                        ],
                        persons=OrderedCaseInsensitiveDict(
                            [('author', [Person('Pronk, Lotte J U'), Person('Medema, Marnix H')])]
                        ),
                    ),
                )
            ]
        ),
        preamble=[],
    )


class TestTiara(ParserTest, TestCase):
    input_string = """
        PMID- 34570171
        OWN - NLM
        STAT- Publisher
        LR  - 20220107
        IS  - 1367-4811 (Electronic)
        IS  - 1367-4803 (Print)
        IS  - 1367-4803 (Linking)
        VI  - 38
        IP  - 2
        DP  - 2021 Sep 27
        TI  - Tiara: Deep learning-based classification system for eukaryotic sequences.
        PG  - 344-50
        LID - btab672 [pii]
        LID - 10.1093/bioinformatics/btab672 [doi]
        AB  - MOTIVATION: With a large number of metagenomic datasets becoming available, 
            eukaryotic metagenomics emerged as a new challenge. The proper classification of 
            eukaryotic nuclear and organellar genomes is an essential step towards a better 
            understanding of eukaryotic diversity. RESULTS: We developed Tiara, a 
            deep-learning-based approach for the identification of eukaryotic sequences in 
            the metagenomic datasets. Its two-step classification process enables the 
            classification of nuclear and organellar eukaryotic fractions and subsequently 
            divides organellar sequences into plastidial and mitochondrial. Using the test 
            dataset, we have shown that Tiara performed similarly to EukRep for prokaryotes 
            classification and outperformed it for eukaryotes classification with lower 
            calculation time. In the tests on the real data, Tiara performed better than 
            EukRep in analysing the small dataset representing eukaryotic cell microbiome and 
            large dataset from the pelagic zone of oceans. Tiara is also the only available 
            tool correctly classifying organellar sequences, which was confirmed by the 
            recovery of nearly complete plastid and mitochondrial genomes from the test data 
            and real metagenomic data. AVAILABILITY: Tiara is implemented in python 3.8, 
            available at https://github.com/ibe-uw/tiara and tested on Unix-based systems. It 
            is released under an open-source MIT license and documentation is available at 
            https://ibe-uw.github.io/tiara. Version 1.0.1 of Tiara has been used for all 
            benchmarks. SUPPLEMENTARY INFORMATION: Supplementary data are available at 
            Bioinformatics online.
        CI  - © The Author(s) 2021. Published by Oxford University Press.
        FAU - Karlicki, Michał
        AU  - Karlicki M
        AD  - Institute of Evolutionary Biology, Faculty of Biology, Biological and Chemical 
            Research Centre, University of Warsaw, ul. Żwirki i Wigury 101, Warszawa, 02-089, 
            Poland.
        FAU - Antonowicz, Stanisław
        AU  - Antonowicz S
        AD  - Institute of Evolutionary Biology, Faculty of Biology, Biological and Chemical 
            Research Centre, University of Warsaw, ul. Żwirki i Wigury 101, Warszawa, 02-089, 
            Poland.
        FAU - Karnkowska, Anna
        AU  - Karnkowska A
        AD  - Institute of Evolutionary Biology, Faculty of Biology, Biological and Chemical 
            Research Centre, University of Warsaw, ul. Żwirki i Wigury 101, Warszawa, 02-089, 
            Poland.
        LA  - eng
        PT  - Journal Article
        DEP - 20210927
        TA  - Bioinformatics
        JT  - Bioinformatics (Oxford, England)
        JID - 9808944
        SB  - IM
        PMC - PMC8722755
        EDAT- 2021/09/28 06:00
        MHDA- 2021/09/28 06:00
        CRDT- 2021/09/27 12:26
        PHST- 2021/03/05 00:00 [received]
        PHST- 2021/08/02 00:00 [revised]
        PHST- 2021/09/21 00:00 [accepted]
        PHST- 2021/09/27 12:26 [entrez]
        PHST- 2021/09/28 06:00 [pubmed]
        PHST- 2021/09/28 06:00 [medline]
        AID - 6375939 [pii]
        AID - btab672 [pii]
        AID - 10.1093/bioinformatics/btab672 [doi]
        PST - aheadofprint
        SO  - Bioinformatics. 2021 Sep 27;38(2):344-50. doi: 10.1093/bioinformatics/btab672.
    """
    correct_result = BibliographyData(
        entries=OrderedCaseInsensitiveDict(
            [
                (
                    'Karlicki2021',
                    Entry(
                        'article',
                        fields=[
                            ('type', 'Journal Article'),
                            ('title', 'Tiara: Deep learning-based classification system for eukaryotic sequences.'),
                            ('journal', 'Bioinformatics (Oxford, England)'),
                            ('date', '2021 Sep 27'),
                            ('volume', '38'),
                            ('pages', '344-50'),
                            ('issn', '1367-4811 (Electronic); 1367-4803 (Print); 1367-4803 (Linking)'),
                            (
                                'abstract',
                                'MOTIVATION: With a large number of metagenomic datasets becoming available,eukaryotic metagenomics emerged as a new challenge. The proper classification ofeukaryotic nuclear and organellar genomes is an essential step towards a betterunderstanding of eukaryotic diversity. RESULTS: We developed Tiara, adeep-learning-based approach for the identification of eukaryotic sequences inthe metagenomic datasets. Its two-step classification process enables theclassification of nuclear and organellar eukaryotic fractions and subsequentlydivides organellar sequences into plastidial and mitochondrial. Using the testdataset, we have shown that Tiara performed similarly to EukRep for prokaryotesclassification and outperformed it for eukaryotes classification with lowercalculation time. In the tests on the real data, Tiara performed better thanEukRep in analysing the small dataset representing eukaryotic cell microbiome andlarge dataset from the pelagic zone of oceans. Tiara is also the only availabletool correctly classifying organellar sequences, which was confirmed by therecovery of nearly complete plastid and mitochondrial genomes from the test dataand real metagenomic data. AVAILABILITY: Tiara is implemented in python 3.8,available at https://github.com/ibe-uw/tiara and tested on Unix-based systems. Itis released under an open-source MIT license and documentation is available athttps://ibe-uw.github.io/tiara. Version 1.0.1 of Tiara has been used for allbenchmarks. SUPPLEMENTARY INFORMATION: Supplementary data are available atBioinformatics online.',
                            ),
                            ('year', '2021'),
                            ('doi', '10.1093/bioinformatics/btab672'),
                            ('PMID', '34570171'),
                            ('OWN', 'NLM'),
                            ('STAT', 'Publisher'),
                            ('LR', '20220107'),
                            ('IP', '2'),
                            ('LID', 'btab672 [pii]; 10.1093/bioinformatics/btab672 [doi]'),
                            ('CI', '© The Author(s) 2021. Published by Oxford University Press.'),
                            ('AU', 'Karlicki M; Antonowicz S; Karnkowska A'),
                            (
                                'AD',
                                'Institute of Evolutionary Biology, Faculty of Biology, Biological and ChemicalResearch Centre, University of Warsaw, ul. Żwirki i Wigury 101, Warszawa, 02-089,Poland.; Institute of Evolutionary Biology, Faculty of Biology, Biological and ChemicalResearch Centre, University of Warsaw, ul. Żwirki i Wigury 101, Warszawa, 02-089,Poland.; Institute of Evolutionary Biology, Faculty of Biology, Biological and ChemicalResearch Centre, University of Warsaw, ul. Żwirki i Wigury 101, Warszawa, 02-089,Poland.',
                            ),
                            ('LA', 'eng'),
                            ('DEP', '20210927'),
                            ('TA', 'Bioinformatics'),
                            ('JID', '9808944'),
                            ('SB', 'IM'),
                            ('PMC', 'PMC8722755'),
                            ('EDAT', '2021/09/28 06:00'),
                            ('MHDA', '2021/09/28 06:00'),
                            ('CRDT', '2021/09/27 12:26'),
                            (
                                'PHST',
                                '2021/03/05 00:00 [received]; 2021/08/02 00:00 [revised]; 2021/09/21 00:00 [accepted]; 2021/09/27 12:26 [entrez]; 2021/09/28 06:00 [pubmed]; 2021/09/28 06:00 [medline]',
                            ),
                            ('PST', 'aheadofprint'),
                            ('SO', 'Bioinformatics. 2021 Sep 27;38(2):344-50. doi: 10.1093/bioinformatics/btab672.'),
                            ('AID', '6375939 [pii]; btab672 [pii]'),
                        ],
                        persons=OrderedCaseInsensitiveDict(
                            [
                                (
                                    'author',
                                    [
                                        Person('Karlicki, Michał'),
                                        Person('Antonowicz, Stanisław'),
                                        Person('Karnkowska, Anna'),
                                    ],
                                )
                            ]
                        ),
                    ),
                )
            ]
        ),
        preamble=[],
    )


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
