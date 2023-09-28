import React, { useState, useEffect } from 'react'
// import { NavLink } from 'react-router-dom';
import 'tailwindcss/tailwind.css';
import UserNavBar from './UserNavBar';
import CardFriend from './CardFriend';

function UserFriends() {
    const [friends, setFriends] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:5555/friends')
        .then((resp) => resp.json())
        .then((data) => {
            setFriends(data)
        })
    }, [])

    const friendsInfo = friends?.map((friend) => {
        return <CardFriend key={friend.id} friend={friend} />
    })

    return (
        <>
            <div className='border-y-2'>
                <UserNavBar />
            </div>
            
            <div className="grid grid-cols-2 gap-4 h-screen bg-white pd-5 pl-[10%]">
                {friendsInfo}
            </div>
        </>
        
    );
}

export default UserFriends;