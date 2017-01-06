MAKEFLAGS += --no-builtin-rules                                                                 
.DEFAULT_GOAL := all
.DELETE_ON_ERROR:
.SUFFIXES:
.PHONY: all dist clean clean-dist

BUILD_DIR := build

all::

dist:: all

clean:: clean-dist
	rm -rf $(BUILD_DIR)

clean-dist::

include $(MAKE_COMMON)/executables/Makefile
include $(MAKE_COMMON)/templates/Makefile-FileSystem
include $(MAKE_COMMON)/templates/Makefile-LaTeX
include make/Makefile-Thesis
