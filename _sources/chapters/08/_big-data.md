# Scaling Big Data Projects

There is a super-linearly increasing amount of data available to us every day.</br>
On the one hand, we can leverage this data to train models with better accuracy.
On the other hand, the increased computational cost required to process this data ask for new techniques: data locality, in-memory computing, and lazy evaluation.

The purpose of this chapter is to introduce different Big Data frameworks available in the Python ecosystem:

- [PySpark](https://spark.apache.org/docs/latest/api/python/#)
- [Dask](https://www.dask.org/)

**Note:** A docker image is available with all dependencies required for this tutorial:

```bash
$ docker pull mathdugre/bigdata-101
$ docker run --rm -it -v $PWD:/app mathdugre/bigdata-101 [args]
```

The container should be launched from the project root; or `$PWD` should be changed accordingly.
<br>By default, the container will run `pytest` command. You can pass extra `[args]` to the container, while launching it.
