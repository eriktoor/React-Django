import React from "react";
import LoginButton from './login-button';
import LogoutButton from "./logout-button";
import Profile from './profile';
import { useAuth0 } from "@auth0/auth0-react";



export default function App () {
    const { user, isAuthenticated, isLoading } = useAuth0();


    return (
        <> 

        { 
        isAuthenticated ? <LogoutButton />  :  <LoginButton />
        }
        
        <p>{JSON.stringify(user)}</p>
        
        <Profile />

        <h1>Hello world from a functional new</h1>        
        </>

    )
}