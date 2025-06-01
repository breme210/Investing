import React from 'react';
import { Link, useLocation } from 'react-router-dom';

const Navigation = () => {
  const location = useLocation();

  const isActive = (path) => {
    return location.pathname === path;
  };

  return (
    <nav className="bg-gray-900 border-b border-gray-700 sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <Link to="/" className="flex items-center space-x-2">
              <div className="w-8 h-8 bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold text-sm">H</span>
              </div>
              <span className="text-white font-semibold text-lg">Hub Editor</span>
            </Link>
          </div>
          
          <div className="flex items-center space-x-8">
            <Link
              to="/"
              className={`px-3 py-2 rounded-md text-sm font-medium transition-colors duration-200 ${
                isActive('/') 
                  ? 'text-white bg-gray-800' 
                  : 'text-gray-300 hover:text-white hover:bg-gray-700'
              }`}
            >
              Home
            </Link>
            <Link
              to="/news"
              className={`px-3 py-2 rounded-md text-sm font-medium transition-colors duration-200 ${
                isActive('/news') || location.pathname.startsWith('/news/')
                  ? 'text-white bg-gray-800' 
                  : 'text-gray-300 hover:text-white hover:bg-gray-700'
              }`}
            >
              News
            </Link>
            <Link
              to="/investments"
              className={`px-3 py-2 rounded-md text-sm font-medium transition-colors duration-200 ${
                isActive('/investments') || location.pathname.startsWith('/investments/')
                  ? 'text-white bg-gray-800' 
                  : 'text-gray-300 hover:text-white hover:bg-gray-700'
              }`}
            >
              Investments
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navigation;