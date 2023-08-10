import React from 'react';

function CardFriend({ friend }) {
    return (
        <div className="border border-gray-300 p-4 my-4 rounded-lg shadow-md">
            <h3 className="text-xl mb-2">{friend.name}</h3>
            <p className="text-gray-600">Email: {friend.email}</p>
        </div>
    );
}

export default CardFriend;