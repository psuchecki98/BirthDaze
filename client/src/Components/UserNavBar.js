import React, { useState } from 'react'
import {AiOutlineClose, AiOutlineMenu, AiOutlineHome} from 'react-icons/ai'
import { NavLink, useNavigate } from 'react-router-dom';

function UserNavBar(){
    const [nav, setNav] = useState(true)

    const handleNav = () => {
        setNav(!nav)
    }

    const navigate = useNavigate();

    function handleHome(e) {
        navigate(`/user`)
    }

    return (
        <div className='flex justify-between items-center'>
            <img 
                onClick={handleNav} 
                className='h-24' 
                src="https://ali-practice-aws-bucket.s3.amazonaws.com/Birthdaze_logo-removebg-preview.png" 
                alt="BIRTHDAZE Logo">
            </img>

            {/* Original look - Found a better one */}
            {/* <ul className='flex hidden'>
                <NavLink key={"UsersHome"} name={"UsersHome"} to={"/user"}>
                    <li  className='p-4 font-bold text-blue-500'>HOME</li>
                </NavLink>

                <NavLink key={"Birthdays"} name={"Birthdays"} to={"/birthdays"}>
                    <li  className='p-4 font-bold text-blue-500'>BIRTHDAYS</li>
                </NavLink>

                <NavLink key={"Friends"} name={"Friends"} to={"/friends"}>
                    <li  className='p-4 font-bold text-blue-500'>FRIENDS</li>
                </NavLink>
            </ul> */}


            <div className='flex space-x-4 px-5'>
                <AiOutlineHome onClick= {handleHome} size={24}/>
                <div onClick={handleNav} className=''>
                    {!nav ? <AiOutlineClose size={24}/> : <AiOutlineMenu size={24}/>}
                </div>
            </div>

            <div className={!nav ? 'fixed left-0 top-0 h-full w-[31%] border-r border-r-gray-900 bg-gray-600' : 'fixed left-[-100%]'}>
                <img onClick={handleNav} className='h-24' src="https://ali-practice-aws-bucket.s3.amazonaws.com/Birthdaze_logo-removebg-preview.png" alt="BIRTHDAZE Logo">
                </img>
                <ul className='p-4'>
                    <NavLink key={"UsersHome"} name={"UsersHome"} to={"/user"}>
                        <li  className='p-3 font-bold border-b border-gray-300 text-blue-500'>HOME</li>
                    </NavLink>

                    <NavLink key={"Birthdays"} name={"Birthdays"} to={"/birthdays"}>
                        <li  className='p-3 font-bold border-b border-gray-300 text-blue-500'>BIRTHDAYS</li>
                    </NavLink>

                    <NavLink key={"Friends"} name={"Friends"} to={"/friends"}>
                        <li  className='p-3 font-bold border-b border-gray-300 text-blue-500'>FRIENDS</li>
                    </NavLink>
                </ul>
            </div>
         </div>

    )
}


export default UserNavBar;