<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/orcunbaslak/pvmodule-el-deduplicator">
    <img src="https://github.com/orcunbaslak/solarian-datalogger/blob/master/images/solarian_logo.png?raw=true" alt="Logo" width="411" height="162">
  </a>

  <h3 align="center">Solarian PV Module EL Image Deduplication Tool</h3>

  <p align="center">
    Solarian PV Module EL Image Deduplication Tools has been written using Python to address the duplicate
    image issues at the PV module manufacturers where modules with different serial numbers have the same
    EL image. This issue has been arised during our regular factory controls and we've developed a tool
    to address it. 
    <br />
    <br />
    <a href="https://github.com/orcunbaslak/pvmodule-el-deduplicator/issues">Report Bug</a>
    ·
    <a href="https://github.com/orcunbaslak/pvmodule-el-deduplicator/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Similar Projects](#similar-projects)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

At Solarian, we are a team of engineers dedicated to offers services of engineering at an exceptional quality. We push our hardest in terms of engineering and analysis.

In order to increase the PV module production quality; we do inspection of photovoltaic modules at the factories. One thing we also check at the factories is duplicate
EL images. Some production facilities tend to use bad software that creates/uses same EL image for different serial numbers. In order to spot those issues we've developed the following code. This software simply checks for similar images using pre-trained MobileNet CNN.

Please feel free to fork or send pull requests. Please keep the code as minimal as possible.

### Built With
This project has been coded with Python 3 using Tensorflow, imagededup and nmslib.
* [Python](https://www.python.org/)
* [tensorflow](https://github.com/tensorflow/tensorflow)
* [imagededup](https://github.com/idealo/imagededup)
* [nmslib](https://github.com/nmslib/nmslib)


<!-- GETTING STARTED -->
## Getting Started

Follow the steps below to prepare the environment for the project.

### Prerequisites

First you need to get Python 3 installed and running with dependencies correctly installed. 
* bash
```sh
sudo apt update
sudo apt-get -y dist-upgrade
sudo apt-get -y install git python3-distutils python3-dev build-essential
sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3 get-pip.py
sudo pip3 install tensorflow imagededup pillow keras
```

### Installation

1. Clone the repo (Change the directory if you want)
```sh
git clone https://github.com/orcunbaslak/pvmodule-el-deduplicator /home/pi/pvmodule-el-deduplicator
```
2. Edit the python file `deduplicate.py` and provide the path to the folder which holds the EL images.
```sh
nano deduplicate.py
```

<!-- USAGE EXAMPLES -->
## Usage

You can feed the file to Python3 interpreter and it's all good to go given you've entered the correct folder path. Please do check the comments in the python file.

```sh
python3 deduplicate.py
```

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/orcunbaslak/pvmodule-el-deduplicator/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewContrib`)
3. Commit your Changes (`git commit -m 'Add a new contribution'`)
4. Push to the Branch (`git push origin feature/NewContrib`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Orçun Başlak - [@orcunbaslak](https://twitter.com/orcunbaslak) - [website](https://orcun.baslak.com/) - orcun.baslak@solarian.com.tr

Solarian Enerji - [@solarianenerji](https://twitter.com/solarianenerji) - [website](https://www.solarian.com.tr/en/) - info@solarian.com.tr

Project Link: [https://github.com/orcunbaslak/pvmodule-el-deduplicator](https://github.com/orcunbaslak/pvmodule-el-deduplicator)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/orcunbaslak/pvmodule-el-deduplicator.svg?style=flat-square
[contributors-url]: https://github.com/orcunbaslak/pvmodule-el-deduplicator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/orcunbaslak/pvmodule-el-deduplicator.svg?style=flat-square
[forks-url]: https://github.com/orcunbaslak/pvmodule-el-deduplicator/network/members
[stars-shield]: https://img.shields.io/github/stars/orcunbaslak/pvmodule-el-deduplicator.svg?style=flat-square
[stars-url]: https://github.com/orcunbaslak/pvmodule-el-deduplicator/stargazers
[issues-shield]: https://img.shields.io/github/issues/orcunbaslak/pvmodule-el-deduplicator.svg?style=flat-square
[issues-url]: https://github.com/orcunbaslak/pvmodule-el-deduplicator/issues
[license-shield]: https://img.shields.io/github/license/orcunbaslak/pvmodule-el-deduplicator.svg?style=flat-square
[license-url]: https://github.com/orcunbaslak/pvmodule-el-deduplicator/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/orcunbaslak