# GCP Initial Setup & First Steps

!!! abstract
    In this hands on you will configure your GCP account, the google cloud SDK and access the cloud console using Google Cloud Shell,
    You will also discover a very useful tool, a managed jupyter notebook service from google named Google Colab which may be very important for your future developments this year

## 1. Create your GCP Account

[Overview link](https://cloud.google.com/docs/overview)

* Create an account within [Google cloud Platform](https://console.cloud.google.com) using your ISAE e-mail
* Use the code given by Dennis to get your free credits
* You should have 300$ + a "free tier" available to you
* From [the interface](https://console.cloud.google.com) you should [create a project](https://cloud.google.com/resource-manager/docs/creating-managing-projects) with a name of your choice

## 2. Install Google Cloud SDK & Configure the shell

If you want to interact with GCP from your computer, you will need to install the [Google Cloud SDK](https://cloud.google.com/sdk), which will also install a shell if you are on windows

If you don't, you will have to do everything from google cloud shell (it's not as easy), so I recommend installing the SDK.

The best ways to interact with google cloud SDK is with a terminal so in that order:

* Linux (either VM or native): <https://cloud.google.com/sdk/docs/install#linux>
* MacOS: <https://cloud.google.com/sdk/docs/install#mac>
* Windows Subsystem for Linux: see Linux
* Windows: <https://cloud.google.com/sdk/docs/install#windows>

If you are on windows, you should launch the google cloud sdk shell now,

Then you can configure the [google cloud sdk](https://cloud.google.com/sdk/docs/initializing) with your account

## 3. My first "VM", Google Cloud Shell

### Intro to Google Cloud Shell

* Google Cloud Shell is a "managed VM" made available to interact with the GCP platform without needing to configure locally the google cloud sdk. It is useful if you only have a web browser, but it may not work and it's not as easy as using a local terminal
* Compared to configured a VM by yourself, this one comes loaded with developer tools and gcp authentification correctly set up, and thus is faster to use,
* However the main drawback to using it as a development machine is the available disk space limited to 5 Gb (not enough to build docker images for example)
* Here is the [description of Google Cloud Shell](https://cloud.google.com/shell)
* Look at the [documentation](https://cloud.google.com/shell/docs/how-cloud-shell-works)

!!! question
    * Can you describe it with your own words ?
    * What would be the closest service that you can find on GCP that is similar to cloud shell ?

### Connect to google cloud shell

![](https://lh3.googleusercontent.com/bADt-LplQDbOD3LLXc8nB4zC5GUjV0MCieIWXOUd7j7gaHL2uDuPuZt3kYdl_KoclG4OHTQp26k=e14-w1502)

* Go to [https://shell.cloud.google.com/](https://shell.cloud.google.com/)
* Follow [this guide](https://cloud.google.com/shell/docs/using-cloud-shell) for connecting to google cloud shell using the browser
* If this doesn't work on your machine for whichever reason, there is a workaround which requires having installed the `google-cloud-sdk`


### Explore google cloud shell

* Check available disk space

??? note "Bash command to run"
    `df -h`

* Check the OS name

??? note "Bash command to run"
    `cat /etc/os-release`

* Check the CPU model

??? note "Bash command to run"
    `cat /proc/cpuinfo`

* This is the hardware model... how many cores do you have available ? Which amount of RAM ?

??? note "Help"
    `htop` will give you your current usage and available cores, or you can do `nproc`

### A demo of cloud shell web preview

We will install [Visual Studio Code Server](https://github.com/cdr/code-server/), which is a cloud-based text editor, on Cloud Shell and preview it from your browser.

There is already a code editor in Google Cloud Shell (based on Theia) but we want to showcase the web preview as well, so we will do it manually,

* You may enable [boost mode](https://cloud.google.com/shell/docs/how-cloud-shell-works#boost_mode)
* Run `curl -fsSL https://code-server.dev/install.sh | sh` in your terminal to download & install code server
* Run `code-server --port=8080` to start code server, it will auto generate a password
* Shut it down (`CTRL+C`) then
* Fetch your password using `cat ~/.config/code-server/config.yaml`
* Re-run it
* [Open web preview on port 8080](https://cloud.google.com/shell/docs/using-web-preview) and log in
* You should be able to open files, get a terminal from inside a vscode inside your browser inside a VM ... Magic isn't it ?

!!! warning
    It is possible that the browser-based method does not work on your machine, there is a [troubleshooting guide on this](https://cloud.google.com/shell/docs/limitations#private_browsing_and_disabled_third-party_cookies) (mainly it doesn't like too much privacy on your browser)

    The alternative solution would be to connect to it from your terminal / local shell using the google cloud sdk,

    Here is the documentation for [this](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell)

    Command to run in this case: `gcloud alpha cloud-shell ssh -- -L 8080:localhost:8080`

!!! why are we using cloud shell ?
    * Cloud Shell is basically a managed VM with the google cloud SDK configured
    * It even has some [nice tools](https://cloud.google.com/shell/docs/how-cloud-shell-works#tools) installed such as docker so you can use it for the next workshops
    * The huge bonus is that it streams through your web browser so it can bypass ISAE-EDU blocking of ssh 
    * However, it may have some stability issues

## 4. Optional - Google Colaboratory

!!! abstract
    Previous versions of this class happened before the ML Class so there was an introduction to google collab. You should have extensively used this tool before, so skip this :)

Here, you will look at Google Colaboratory, which is a very handy tool for doing data science work (based on jupyter notebooks) on the cloud, using a preconfigured instance (which can access a GPU). You will be able to store data on Google Drive and to share

**I highly recommend using this for Jupyter based AML BE**, but I invite you to discover google colab *at home, or during AML BE* because it's a useful tool but mastering it is not relevant for our cloud class

### Intro & Description of Google Colaboratory

* Open [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb)
* [Some intro](https://ledatascientist.com/google-colab-le-guide-ultime/), [another one](https://towardsdatascience.com/getting-started-with-google-colab-f2fff97f594c)

!!! question
    - Can you describe what it is ?
    - Is it IaaS ? PaaS ? SaaS ? why exactly ?

!!! info
    Colaboratory, or "Colab" for short, allows you to write and execute Python in your browser, with

    * Zero configuration required
    * Free access to GPUs
    * Easy sharing

    It offers a "jupyter notebook - like" interface, and allows to install your own dependencies by running bash commands inside the VM, with connection to google drive, google sheets

    You can manipulate the notebooks from your Google Drive and share it like it was a GDoc document

    It's essentially between SaaS and PaaS, it offers you a development platform without you having to manage anything except your code and your data (which are both data from the cloud provider point of view)

### Loading jupyter notebooks, interacting with google drive

* Open a notebook you previously ran on your computer (from AML class), you can [run a notebook on github directly in google colab](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipOther references:ynb)
* Try to run it inside google colab
* Link [google colab and google drive](https://colab.research.google.com/notebooks/io.ipynb) and upload something on google drive (like an image) and display in on google colab

### Other nice usages of Google Colab

* [Writing markdown to generate reports](https://colab.research.google.com/notebooks/markdown_guide.ipynb)
* [Installing custom dependencies](https://colab.research.google.com/notebooks/snippets/importing_libraries.ipynb)
