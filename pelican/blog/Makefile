PELICAN=pelican
#PELICANOPTS= -t bootstrap2
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(CURDIR)/content
OUTPUTDIR=$(BASEDIR)/output
#OUTPUTDIR=/srv/http
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py
PUBLISHCONFLOCAL=$(BASEDIR)/publishconflocal.py

FTP_HOST=localhost
FTP_USER=anonymous
FTP_TARGET_DIR=/

#SSH_HOST=wilkesley.org
SSH_PORT=22
SSH_USER=ian
#SSH_TARGET_DIR=/home/ian/public_html/journal/

DROPBOX_DIR=~/Dropbox/Public/

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html                        (re)generate the web site          '
	@echo '   make clean                       remove the generated files         '
	@echo '   make regenerate                  regenerate files upon modification '
	@echo '   make publish                     generate using production settings '
	@echo '   make serve                       serve site at http://localhost:8000'
	@echo '   make devserver                   start/restart develop_server.sh    '
	@echo '   github                           upload the web site via gh-pages   '
	@echo '   local				   publish locally and start server   '
	@echo '                                                                       '


html: clean $(OUTPUTDIR)/index.html
	@echo 'Done'

$(OUTPUTDIR)/%.html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	find $(OUTPUTDIR) -mindepth 1 -delete

regenerate: clean
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
	cd $(OUTPUTDIR) && python -m http.server 8100

devserver:
	$(BASEDIR)/develop_server.sh restart

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

github: publish
	ghp-import $(OUTPUTDIR)
	git push origin gh-pages

local:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONFLOCAL)
	cd $(OUTPUTDIR) && python -m http.server 8100


.PHONY: html help clean regenerate serve devserver publish github local
