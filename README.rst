=======
OMXWare
=======

.. image:: https://travis.ibm.com/GrandChallenge-Almaden/omxware-pypi.svg?token=zra2vLszsZmyB2CQTsas&branch=master
    :target: https://travis.ibm.com/GrandChallenge-Almaden/omxware-pypi


.. image:: https://badge.fury.io/py/omxware.svg
    :target: https://badge.fury.io/py/omxware
    :alt: Latest Version

|

**Web Services**

`http://ibm.biz/omxware-api <https://api.s2s-omxware.us-south.containers.appdomain.cloud/>`_

---------------

**SDK Documentation:**

`http://ibm.biz/omxware-sdk-docs <https://ibm.github.io/omxware-pypi-docs/>`_

---------------

**Getting Started**

`https://ibm.github.io/omxware-pypi-docs/build/html/usage.html <https://ibm.github.io/omxware-pypi-docs/build/html/usage.html>`_

---------------

**Help / Forums**

`http://ibm.biz/omxware-forum <https://forum.s2s-omxware.us-south.containers.appdomain.cloud>`_

---------------

Citation
***************
* Please contact the `OMXWare Team via the Forums <http://ibm.biz/omxware-citation>`_ for updated citation information prior to publishing or presenting OMXWare content.

 e.g: ``"OMXWare: Microbial Life at Scale" IBM Research, manuscript in preparation``

|

Use with Docker
***************


In an effort to make it easier for users and developers to get started with OMXWare, We have a 2 base docker images with ``python`` and OMXWare pre-installed. It also comes with a bunch of python libs like ``matplotlib``, ``numpy`` along with some others.

 **1)  Minimal:** ``docker pull c0mpiler/alpine-omxware-base:latest``

----------------------------------------------------------------------------------------------------------------------

            .. code-block:: bash

             docker run -it --rm --name omxware -v "$(pwd):/opt/my_work" c0mpiler/alpine-omxware-base:latest ash

----------------------------------------------------------------------------------------------------------------------

        * This is a relatively small docker image with just the required packages / libraries installed and setup.
        * Change the mount point to whatever you want on you host machine.
        * You may use this image as a base to build other docker containers / applications. Refer to: https://github.com/c0mpiler/alpine-omxware-base/blob/master/Dockerfile for specifics.

|

 **2)  JupyterLab:** ``docker pull c0mpiler/jupyter:latest``

---------------------------------------------------------------------------------------------------------

            .. code-block:: bash

             docker run -d --name jupyter --restart always -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes \
             -v /mnt/storage/jupyter:/home/jovyan/work c0mpiler/jupyter start.sh jupyter lab --LabApp.token=‘omxware’

---------------------------------------------------------------------------------------------------------

        * This image has JupyterLab pre-installed and setup with some example OMXWare Jupyter notebooks.
        * Change the mount point ``/mnt/storage/jupyter`` to whatever you want on you host machine – so you can share files from your host with this docker image.

        * This image also has some example Jupyter notebooks for you to look at and get started.

        * Once you run the docker image – you can open up ``http://<host-name>:8888/lab?`` in your browser and the pwd is ``omxware``.

        * The host-name is that of your host machine you run this docker image on. If you are running it on your laptop, the host-name is either ``localhost`` or ``0.0.0.0``
