Bootstrap:docker
From:ubuntu:17.04

%post
	apt-get update
	DEBIAN_FRONTEND=noninteractive \
	apt-get install -y --no-install-recommends \
		ninja-build \
		texlive-latex-base \
		texlive-latex-recommended \
		texlive-latex-extra \
		texlive-fonts-recommended \
		texlive-fonts-extra \
		texlive-science \
		texlive-publishers
	rm -rf /var/lib/apt/lists/*
