Bootstrap:docker
From:ubuntu:17.04

%post
	apt-get update -qq
	apt-get install wget software-properties-common apt-transport-https -y
	sh -c "wget -O - http://dl.openfoam.org/gpg.key | apt-key add -"
	add-apt-repository "http://dl.openfoam.org/ubuntu dev" -y
	add-apt-repository 'deb http://atmosfoam-apt.s3-website-eu-west-1.amazonaws.com dev main' -y
	apt-get update -qq
	DEBIAN_FRONTEND=noninteractive \
        apt-get install -y --no-install-recommends \
               ninja-build \
               texlive-latex-base \
               texlive-latex-recommended \
               texlive-latex-extra \
               texlive-fonts-recommended \
               texlive-fonts-extra \
               texlive-font-utils \
               texlive-science \
               texlive-publishers \
               ghostscript \
               gnuplot
	DEBIAN_FRONTEND=noninteractive \
	apt-get install openfoam-dev -y --no-install-recommends
	apt-get install atmosfoam-tools -y --allow-unauthenticated
	rm -rf /var/lib/apt/lists/*
