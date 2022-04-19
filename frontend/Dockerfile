FROM node:lts-alpine
COPY ./airconditioner /airconditioner
WORKDIR /airconditioner
RUN yarn install
RUN chown -R node:node /airconditioner
user node
EXPOSE 8080
CMD ["yarn", "serve"]
