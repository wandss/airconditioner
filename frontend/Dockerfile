FROM node:lts-alpine
COPY ./airconditioner /airconditioner
WORKDIR /airconditioner
RUN yarn install
EXPOSE 8080
CMD ["yarn", "serve"]
