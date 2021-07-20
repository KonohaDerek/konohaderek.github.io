FROM klakegg/hugo:alpine as hugo

RUN apk update && apk upgrade && \
  apk add --no-cache bash git openssh vim

ENTRYPOINT ["tail"]
CMD ["-f","/dev/null"]

# ENTRYPOINT ["bash" , "tail -f /dev/null"]
