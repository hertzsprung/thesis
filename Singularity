Bootstrap:docker
From:ubuntu:17.04

%environment
	DEBIAN_FRONTEND=noninteractive
	LANG=en_GB.UTF-8
	LANGUAGE=en_GB:en
	LC_ALL=en_GB.UTF-8
	export DEBIAN_FRONTEND

%post
	apt-get update
	apt-get install -y --no-install-recommends \
		git \
		ca-certificates \
		ninja-build \
		texlive-latex-base \
		texlive-latex-recommended \
		texlive-latex-extra \
		texlive-fonts-recommended \
		texlive-fonts-extra \
		texlive-science
	rm -rf /var/lib/apt/lists/*
	git clone --branch master https://github.com/hertzsprung/thesis.git /opt/thesis

%test
	/bin/true
