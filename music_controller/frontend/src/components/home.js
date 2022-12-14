import { BrowserRouter as Router, Link, Redirect } from "react-router-dom";
import React from "react";
import { useAuth0 } from "@auth0/auth0-react";
import LogoutButton from "./logout-button";
import LoginButton from "./login-button";

const HomePage = () => {
  const { user, isAuthenticated, isLoading } = useAuth0();

  if (isLoading) {
    return <div>Loading ...</div>;
  }

  return (
    <>
      <p>Welcome to this site</p>
      {isAuthenticated && !isLoading ? <LogoutButton /> : <LoginButton />}
      <Link to="/profile">Check out the profile page</Link>
    </>
  );
};

export default HomePage;
