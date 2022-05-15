import { ApolloClient, InMemoryCache } from "@apollo/client";

// Apollo Client connection with Backend
const client = new ApolloClient({
  uri: "http://127.0.0.1:8000/gql/",
  cache: new InMemoryCache(),
});
export default client;
