set :stages, %w(prod)
set :default_stage, "prod"
require 'capistrano/ext/multistage'
require "capistrano-postgresql"

set :application, "storelist"

set :repository,  "git@github.com:Leeaandrob/store-list-backend.git"
#ssh_options[:forward_agent] = true
#default_run_options[:pty] = true

set :branch, "master"

set :user, "root"
set :use_sudo, true

set :keep_releases, 3


set :deploy_to, "/home/webapps/#{application}"
set :copy_dir, "/tmp"
set :copy_remote_dir, "/tmp"

set :scm, :git

set :postgresql_database, "storelist_db"
set :postgresql_user, "storelist"
set :postgresql_password, "qwert741258"

after "deploy", "deploy:cleanup"

namespace :deploy do
	task :finalize_update do
	end

	task :restart_app do
		run "sudo supervisorctl restart storelist"
		run "sudo supervisorctl restart celery"
		run "sudo service nginx restart"
	end

	desc "Atualizacao e instalacao de depedencias para o projeto"
	task :setup do
		path_files = '/home/webapps'
		run "echo Setup Server"
		run "sudo mkdir -p /home/webapps/storelist /home/webapps/storelist/releases /home/webapps/storelist/shared /home/webapps/storelist/shared/system /home/webapps/storelist/shared/log /home/webapps/storelist/shared/pids"
		run "sudo chmod g+w /home/webapps/storelist /home/webapps/storelist/releases /home/webapps/storelist/shared /home/webapps/storelist/shared/system /home/webapps/storelist/shared/log /home/webapps/storelist/shared/pids"
		run "echo Atualizando"
		run "sudo apt-get -y upgrade && apt-get -y update"
		run "apt-get -y install python-dev python2.7-dev python-virtualenv postgresql postgresql-contrib libpq-dev nginx supervisor rabbitmq-server libreadline-dev libncurses5-dev libffi-dev libxml2-dev libxslt1-dev git nodejs npm nodejs-legacy libjpeg-dev zlib1g-dev libpng12-dev"
		run "ln -s -f shared/log/ #{deploy_to}/logs"
		run "echo Configurando"
		run "cd #{deploy_to} && virtualenv . "
		run "sudo mv -f #{path_files}/gunicorn_start.bash #{deploy_to}/bin/"
		run "touch #{deploy_to}/logs/gunicorn_supervisor.log"
		run "sudo chmod u+x #{deploy_to}/bin/gunicorn_start.bash"
		run "sudo mv -f #{path_files}/storelist.conf /etc/nginx/sites-enabled/"
		run "sudo ln -s -f /etc/nginx/sites-enabled/storelist.conf /etc/nginx/sites-available/storelist.conf"
		run "sudo mv -f #{path_files}/storelist_supervisor.conf /etc/supervisor/conf.d/"
	end

	task :restart, :roles => :app do
		python_path = "#{deploy_to}/bin/python"
		run "echo baz"
		run "#{deploy_to}/bin/pip install -r #{deploy_to}/current/requirements_production.txt"
		run "#{python_path} #{deploy_to}/current/storelist/manage.py migrate --settings=storelist.settings_production"
		run "rm #{deploy_to}/current/storelist/**/migrations/*[0-9]*.py && rm #{deploy_to}/current/storelist/**/migrations/*[0-9]*.pyc"
		run "#{python_path} #{deploy_to}/current/storelist/manage.py makemigrations --settings=storelist.settings_production"
		run "#{python_path} #{deploy_to}/current/storelist/manage.py collectstatic -v0 --noinput --settings=storelist.settings_production"
		run "cd #{deploy_to} && sudo chown -h webapps:webapps current"
		run "cd #{deploy_to} && sudo chown -h webapps:webapps current/*"
	end
end