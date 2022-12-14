import App from "./components/App";
import React from "react";
import ReactDOM from "react-dom";
import { Auth0Provider } from "@auth0/auth0-react";

const root = ReactDOM.createRoot(document.getElementById("app"));

root.render(
  <Auth0Provider
    domain="dev-rbyiwhiira2b3jhv.us.auth0.com"
    clientId="8FebehmOLZYNXc6g65OXeAeTgkVrA9Vd"
    redirectUri={window.location.origin} // should be window.location.origin
    accessType="offline" // what is this ?
  >
    <App />
  </Auth0Provider>
);
