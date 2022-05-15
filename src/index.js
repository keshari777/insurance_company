import React from "react";
import "./index.css";
import App from "./App";
import { ApolloProvider } from "@apollo/client";
import client from "./utils/client";
import reportWebVitals from "./reportWebVitals";
import { createRoot } from "react-dom/client";
import "antd/dist/antd.css";

const container = document.getElementById("root");
const root = createRoot(container);
root.render(
  <ApolloProvider client={client}>
    <App />
  </ApolloProvider>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
