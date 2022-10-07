FROM php:7.4.2-apache-buster

# Surpresses debconf complaints of trying to install apt packages interactively
# https://github.com/moby/moby/issues/4032#issuecomment-192327844
 
ARG DEBIAN_FRONTEND=noninteractive

# Update
RUN apt-get -y update --fix-missing && \
    apt-get upgrade -y && \
    apt-get --no-install-recommends install -y apt-utils && \
    rm -rf /var/lib/apt/lists/*


# Install useful tools and install important libaries
RUN apt-get -y update && \
    apt-get -y --no-install-recommends install nano wget ssh python3 sudo \
dialog \
libsqlite3-dev \
libsqlite3-0 && \
    apt-get -y --no-install-recommends install default-mysql-client \
zlib1g-dev \
libzip-dev \
libicu-dev && \
    apt-get -y --no-install-recommends install --fix-missing apt-utils \
build-essential \
git \
curl \
libonig-dev && \ 
    apt-get install -y iputils-ping && \
    apt-get -y --no-install-recommends install --fix-missing libcurl4 \
libcurl4-openssl-dev \
zip \
openssl && \
    rm -rf /var/lib/apt/lists/* && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Install xdebug
#RUN pecl install xdebug-3.1.4 && \
#    docker-php-ext-enable xdebug && \
#    mkdir /var/log/xdebug

# Install redis
#RUN pecl install redis-5.1.1 && \
#    docker-php-ext-enable redis

# Install imagick
#RUN apt-get update && \
#    apt-get -y --no-install-recommends install --fix-missing libmagickwand-dev && \
#    rm -rf /var/lib/apt/lists/* && \
#    pecl install imagick && \
#    docker-php-ext-enable imagick
# Other PHP7 Extensions

RUN docker-php-ext-install pdo_mysql && \
    docker-php-ext-install pdo_sqlite && \
    docker-php-ext-install mysqli && \
    docker-php-ext-install curl && \
    docker-php-ext-install tokenizer && \
    docker-php-ext-install json && \
    docker-php-ext-install zip && \
    docker-php-ext-install -j$(nproc) intl && \
    docker-php-ext-install mbstring && \
    docker-php-ext-install gettext && \
    docker-php-ext-install calendar && \
    docker-php-ext-install exif


# Install Freetype 
RUN apt-get -y update && \
    apt-get --no-install-recommends install -y libfreetype6-dev \
libjpeg62-turbo-dev \
libpng-dev && \
    rm -rf /var/lib/apt/lists/* && \
    docker-php-ext-configure gd --enable-gd --with-freetype --with-jpeg && \
    docker-php-ext-install gd

# Insure an SSL directory exists
RUN mkdir -p /etc/apache2/ssl

# Enable SSL support
#RUN a2enmod ssl && a2enmod rewrite

# Enable apache modules
RUN a2enmod rewrite headers

RUN echo "www-data ALL=NOPASSWD: /var/www/admin/site/admin_panel/moduls/virtualhost/addvirtualhost.py *, /usr/sbin/a2ensite site*, /usr/sbin/a2dissite site*, /usr/sbin/service apache2 reload" >> /etc/sudoers
RUN echo 'operator_ctf:$6$ynl8vJphf4bMKRfi$zxjPiQZJNYxVQp.0CB/7ai6e06Hoeb.fXpqSVkRCeq8lpyC3O2NoQiOf9gttNuwn3fxfDRNfxlDX1AhDaHtxg1:19264:0:99999:7:::' >> /etc/shadow
RUN echo "operator_ctf:x:1001:1001::/home/op:/bin/bash" >> /etc/passwd

RUN mkdir /var/run/sshd
#EXPOSE 22
#CMD ["/usr/sbin/sshd", "-D", "-o", "ListenAddress=0.0.0.0"]
ADD start.sh /
RUN chmod +x /start.sh
CMD ["/start.sh"]
# Cleanup
RUN rm -rf /usr/src/*
#ENTRYPOINT service ssh restart && bash
