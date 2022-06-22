# Tools of Big Data

The amount of data in the world, the form these data take, and the ways to
interact with data have all increased exponentially in recent years. The
extraction of useful knowledge from data has long been one of the grand
challenges of computer science, and the dawn of "big data" has transformed the
landscape of data storage, manipulation, and analysis. In this module, we will
look at the tools used to store and interact with data.

The objective of this class is that students gain:

+ First hand experience with and detailed knowledge of computing models, notably cloud computing
+ An understanding of distributed programming models and data distribution
+ Broad knowledge of many databases and their respective strengths

As a part of the [Data and Decision Sciences](https://supaerodatascience.github.io/)
Master's program, this module aims specifically at providing the tool set
students will use for data analysis and knowledge extraction using skills
acquired in the Algorithms of Machine Learning and Digital Economy and Data Uses
classes.

## Class structure

The class is structured in three parts:

### Data computation

  20 hours on the computing platforms used in the data ecosystem. We will
  briefly cover cluster computing and then go in depth on cloud computing, using
  Google Cloud Platform as an example. Finally, a class on GPU computing will be
  given in coordination with the deep learning section of the AML class.

### Data distribution

  20 hours on the distribution of data, with a focus on distributed programming
  models. We will introduce functional programming and MapReduce, then use these
  concepts in a practical session on Spark. Finally, students will do a graded
  exercise with Dask.

### Databases

  In the final 10 hours of the course, state-of-the-art databases will be
  presented. Students will install and demonstrate the advantages of different
  databases to their peers as a graded project.

## Class schedule

Class dates are subject to change. Please refer to Hyerplng for detailed scheduling.

Introduction | | | |
--- | --- | --- | ---
[Introduction to tools of Big Data](1_introduction) | 2h | 29/09/2020 | [Global Datasphere](readings/idc_data.pdf)

Data Computation | | | |
--- | --- | --- | ---
[Cloud Computing & Google Cloud Platform](2_data_computation/site/#cloud-computing-4h) | 2h <br />2h | 07/10/2020 <br /> 14/10/2020| [Readings](2_data_computation/site/7_readings/#about-cloud-computing)
[Containers](2_data_computation/site/#containers-2h) | 2h| 14/10/2020| [Readings](2_data_computation/site/7_readings/#about-orchestration)
[Orchestration](2_data_computation#orchestration-deployment-1h) | 1h | 20/10/2020 | [Readings](2_data_computation/site/7_readings/#about-containers) |
[BE](2_data_computation/site/#final-be-3h) | 3h | 20/10/2020 | *TBD*
Cluster Computing | 2h | TBD| [SLURM](readings/slurm.pdf)
GPU computing, part 1 | 3h | 01/12/2020 | [GPGPU TP](https://lms.isae.fr/course/view.php?id=1226&section=2) |
GPU computing, part 2 | 3h | 02/12/2020 | [GPGPU TP](https://lms.isae.fr/course/view.php?id=1226&section=2) |


| Data Distribution | | | Readings |
| --- | --- | --- | --- |
| [Hadoop and MapReduce](2_3_mapreduce.md) | 3h | 08/02/2022 | [MapReduce](https://raw.githubusercontent.com/SupaeroDataScience/OBD/master/readings/mapreduce.pdf) |
| [Spark](2_4_spark.md) | 4h | 08/02/2022 | [Spark](https://raw.githubusercontent.com/SupaeroDataScience/OBD/master/readings/spark.pdf) [PySpark](https://spark.apache.org/docs/latest/api/python/pyspark.html) |
| [Dask on Kubernetes](2_5_dask.md)| 3h | 14/02/2022 | [Dask documentation](https://docs.dask.org/en/latest/setup/kubernetes.html) |
| [Dask project](2_6_project.md) | 6h | 16/02/2022 | [Dask](https://raw.githubusercontent.com/SupaeroDataScience/OBD/master/readings/dask.pdf) |


Databases | | | |
--- | --- | --- | ---
Databases overview | 2h | 03/02/2021 | [Database Systems](readings/fntdb07-architecture.pdf)
PostgeSQL TP | 3h | 08/02/2021 | [PostgeSQL](https://www.postgresql.org/docs/manuals/)
Project overview | 2h | 15/02/2021 |
Project presentations | 2h | 08/03/2021 |

## Use with Binder

Some of the notebooks from this class (Julia, Spark ...) can be launched with MyBinder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/SupaeroDataScience/OBD/master?urlpath=lab)
