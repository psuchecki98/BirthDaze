import React, { useContext } from 'react'
// import { NavLink } from 'react-router-dom';
import 'tailwindcss/tailwind.css';
import UserNavBar from './UserNavBar';
import UserContext from '../Context/UserContext';

function UserHomePage() {
    
    const { user } = useContext(UserContext)
    
    return (
        <div className="flex flex-col h-screen bg-white">
            <div className='border-y-2'>
                <UserNavBar />
            </div>
            <div className="flex-grow flex flex-col justify-center items-center">
                <h1 className="text-5xl font-bold text-gray-700 mb-6">
                    Welcome {user}!
                </h1>
                <h2 className="text-2xl text-blue-500 mb-12">
                    Here's what's coming up:
                </h2>
                <div className="w-3/4 bg-gray-100 p-6 rounded-lg shadow-lg">
                    <h3 className="text-xl font-bold mb-4">
                        Upcoming Birthdays:
                    </h3>
                    <p className="mb-2">  John Doe: 25th July</p>
                    <p className="mb-2">  Jane Smith: 30th July</p>
                    <p className="mb-2">  Alice Johnson: 5th August</p>
                </div>
            </div>
        </div>
    );
}


export default UserHomePage;