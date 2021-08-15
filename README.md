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
  <a href="https://github.com/orcunbaslak/pvsyst-elevation">
    <img src="https://github.com/orcunbaslak/solarian-datalogger/blob/master/images/solarian_logo.png?raw=true" alt="Logo" width="411" height="162">
  </a>

  <h3 align="center">Solarian PVSYST Elevation Tool</h3>

  <p align="center">
    Solarian PVSYST elevation tool is a tool writter in Python that grabs the elevation profile of a 
    location given the bottom left and top right coordinates. The CSV output file can directly be imported 
    into PVSYST software. 
    <br />
    <br />
    <a href="https://github.com/orcunbaslak/pvsyst-elevation/issues">Report Bug</a>
    ·
    <a href="https://github.com/orcunbaslak/pvsyst-elevation/issues">Request Feature</a>
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

3D terrain geometry is essential in simulating solar power plants to correctly simulate the shading and get to the correct results. This software pulls values from international elevation databases and provides the CSV file that PVSYST can import. Although this data is not very accurate; It can provide the engineer with sufficient inclination (general topology) of the area.

Please feel free to fork or send pull requests. Please keep the code as minimal as possible.

### Built With
This project has been coded with Python 3 using OSGeo GDAL, elevation and GeoPy.
* [Python](https://www.python.org/)
* [gdal](https://github.com/OSGeo/gdal)
* [elevation](https://github.com/bopen/elevation)
* [geopy](https://github.com/geopy/geopy)


<!-- GETTING STARTED -->
## Getting Started

Follow the steps below to prepare the environment for the project.

### Prerequisites

First you need to get Python 3 installed and running with dependencies correctly installed. Please check your system-wide installed GDal version and install the same version for python.
* bash
```sh
sudo apt update
sudo apt-get -y dist-upgrade
sudo apt-get -y install git python3-distutils python3-dev curl unzip gdal-bin libgdal-dev build-essential
sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3 get-pip.py
sudo pip3 install elevation rasterio fiona pandas gdal==2.4.0 geopy
```

### Installation

1. Clone the repo (Change the directory if you want)
```sh
git clone https://github.com/orcunbaslak/pvsyst-elevation /home/pi/pvsyst-elevation
```
2. Edit the python file `pvsyst-evelation.py` and insert coordinates.
```sh
nano pvsyst-evelation.py
```

<!-- USAGE EXAMPLES -->
## Usage

You can feed the file to Python3 interpreter and it's all good to go given you've entered the correct coordinates. Please do check the comments in the python file.

```sh
python3 pvsyst-elevation.py
```

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/orcunbaslak/pvsyst-evelation/issues) for a list of proposed features (and known issues).



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

Distributed under the GNU GPL v3 License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Orçun Başlak - [@orcunbaslak](https://twitter.com/orcunbaslak) - [website](https://orcun.baslak.com/) - orcun.baslak@solarian.com.tr

Solarian Enerji - [@solarianenerji](https://twitter.com/solarianenerji) - [website](https://www.solarian.com.tr/en/) - info@solarian.com.tr

Project Link: [https://github.com/orcunbaslak/pvsyst-elevation](https://github.com/orcunbaslak/pvsyst-elevation)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/orcunbaslak/pvsyst-elevation.svg?style=flat-square
[contributors-url]: https://github.com/orcunbaslak/pvsyst-elevation/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/orcunbaslak/pvsyst-elevation.svg?style=flat-square
[forks-url]: https://github.com/orcunbaslak/pvsyst-elevation/network/members
[stars-shield]: https://img.shields.io/github/stars/orcunbaslak/pvsyst-elevation.svg?style=flat-square
[stars-url]: https://github.com/orcunbaslak/pvsyst-elevation/stargazers
[issues-shield]: https://img.shields.io/github/issues/orcunbaslak/pvsyst-elevation.svg?style=flat-square
[issues-url]: https://github.com/orcunbaslak/pvsyst-elevation/issues
[license-shield]: https://img.shields.io/github/license/orcunbaslak/pvsyst-elevation.svg?style=flat-square
[license-url]: https://github.com/orcunbaslak/pvsyst-elevation/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/orcunbaslak