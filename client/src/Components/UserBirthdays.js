import React from 'react'
// import { NavLink } from 'react-router-dom';
import 'tailwindcss/tailwind.css';
import UserNavBar from './UserNavBar';

function UserBirthdays() {
    return (
        <div className="flex flex-col h-screen bg-white">
            <div className='border-y-2'>
                <UserNavBar />
            </div>
        </div>
    );
}

export default UserBirthdays;