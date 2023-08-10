import React from 'react'
import {} from 'react-icons'
import { NavLink } from 'react-router-dom';

function NavBar(){
    return (
        <div className='flex justify-between items-center h-24 mx-auto px-4'>
            <img className='h-24' src="https://ali-practice-aws-bucket.s3.amazonaws.com/Birthdaze_logo-removebg-preview.png" alt="BIRTHDAZE Logo">
            </img>
            <ul className='flex'>
                <NavLink key={"Home"} name={"Home"} to={"/"}>
                    <li  className='p-4 font-bold text-blue-500'>HOME</li>
                </NavLink>

                <NavLink key={"Features"} name={"Features"} to={"/features"}>
                    <li  className='p-4 font-bold text-blue-500'>FEATURES</li>
                </NavLink>

                <NavLink key={"SignIn"} name={"SignIn"} to={"/signin"}>
                    <li  className='p-4 font-bold text-blue-500'>LOGIN</li>
                </NavLink>
            </ul>
        </div>
    )
}

export default NavBar;