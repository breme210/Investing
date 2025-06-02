import React from 'react';
import { Link } from 'react-router-dom';

const NewsCard = ({ article }) => {
  const formatDate = (dateString) => {
    const date = new Date(dateString);
    const now = new Date();
    const diffTime = Math.abs(now - date);
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    
    if (diffDays === 1) return 'Today';
    if (diffDays === 2) return 'Yesterday';
    if (diffDays <= 7) return `${diffDays - 1} days ago`;
    
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    });
  };

  const getCategoryConfig = (category) => {
    const configs = {
      'Technology': { 
        color: 'bg-gradient-to-r from-blue-500 to-blue-600', 
        icon: '💻',
        description: 'Tech News'
      },
      'Product Updates': { 
        color: 'bg-gradient-to-r from-green-500 to-green-600', 
        icon: '🚀',
        description: 'Product Updates'
      },
      'Industry News': { 
        color: 'bg-gradient-to-r from-purple-500 to-purple-600', 
        icon: '🏢',
        description: 'Industry'
      },
      'Company News': { 
        color: 'bg-gradient-to-r from-orange-500 to-orange-600', 
        icon: '📢',
        description: 'Company'
      },
      'Market Analysis': { 
        color: 'bg-gradient-to-r from-red-500 to-red-600', 
        icon: '📊',
        description: 'Markets'
      },
      'Financial': { 
        color: 'bg-gradient-to-r from-yellow-500 to-yellow-600', 
        icon: '💰',
        description: 'Finance'
      }
    };
    return configs[category] || { 
      color: 'bg-gradient-to-r from-gray-500 to-gray-600', 
      icon: '📰',
      description: 'News'
    };
  };

  // Get appropriate image based on category or use provided image
  const getImageForCategory = (category) => {
    const images = {
      'Technology': 'https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
      'Product Updates': 'https://images.unsplash.com/photo-1531297484001-80022131f5a1?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
      'Industry News': 'https://images.unsplash.com/photo-1504711434969-e33886168f5c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
      'Company News': 'https://images.pexels.com/photos/7054384/pexels-photo-7054384.jpeg?auto=compress&cs=tinysrgb&w=800',
      'Market Analysis': 'https://images.pexels.com/photos/590022/pexels-photo-590022.jpeg',
      'Financial': 'https://images.unsplash.com/photo-1579621970563-ebec7560ff3e'
    };
    return images[category] || images['Technology'];
  };

  const categoryConfig = getCategoryConfig(article.category);

  return (
    <Link to={`/news/${article.id}`} className="block group">
      <article className="card group-hover:scale-105 group-hover:border-blue-500/50 transition-all duration-300 overflow-hidden p-0">
        {/* Image Section */}
        <div className="relative overflow-hidden">
          <img
            src={article.image_url || getImageForCategory(article.category)}
            alt={article.title}
            className="w-full h-48 object-cover group-hover:scale-110 transition-transform duration-500"
          />
          
          {/* Overlay with Category Badge */}
          <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent"></div>
          
          {/* Category Badge */}
          <div className="absolute top-4 left-4">
            <div className={`${categoryConfig.color} text-white px-3 py-1.5 rounded-xl text-xs font-bold shadow-lg flex items-center space-x-1`}>
              <span>{categoryConfig.icon}</span>
              <span>{categoryConfig.description}</span>
            </div>
          </div>
          
          {/* Read Time Badge */}
          <div className="absolute top-4 right-4">
            <div className="bg-black/50 backdrop-blur-sm text-white px-3 py-1.5 rounded-xl text-xs font-medium">
              ⏱️ {article.read_time} min read
            </div>
          </div>
        </div>
        
        {/* Content Section */}
        <div className="p-6">
          {/* Title */}
          <h3 className="text-xl font-bold text-white mb-3 group-hover:text-blue-400 transition-colors duration-200 line-clamp-2 leading-tight">
            {article.title}
          </h3>
          
          {/* Summary */}
          <p className="text-gray-400 mb-4 line-clamp-3 leading-relaxed">
            {article.summary}
          </p>
          
          {/* Tags */}
          {article.tags && article.tags.length > 0 && (
            <div className="mb-4 flex flex-wrap gap-2">
              {article.tags.slice(0, 3).map((tag, index) => (
                <span
                  key={index}
                  className="px-2 py-1 bg-gray-700/50 text-gray-300 text-xs rounded-lg border border-gray-600"
                >
                  #{tag}
                </span>
              ))}
              {article.tags.length > 3 && (
                <span className="px-2 py-1 bg-gray-700/50 text-gray-400 text-xs rounded-lg border border-gray-600">
                  +{article.tags.length - 3} more
                </span>
              )}
            </div>
          )}
          
          {/* Footer */}
          <div className="flex items-center justify-between pt-4 border-t border-gray-700">
            <div className="flex items-center space-x-2">
              <div className="w-8 h-8 bg-gradient-to-r from-blue-500 to-purple-600 rounded-full flex items-center justify-center">
                <span className="text-white text-xs font-bold">
                  {article.author.charAt(0).toUpperCase()}
                </span>
              </div>
              <div>
                <span className="text-gray-300 text-sm font-medium">{article.author}</span>
              </div>
            </div>
            
            <div className="text-right">
              <div className="flex items-center space-x-1 text-gray-400 text-sm">
                <span>🕒</span>
                <span>{formatDate(article.publish_date)}</span>
              </div>
            </div>
          </div>
          
          {/* Read More Indicator */}
          <div className="mt-4 flex items-center text-blue-400 group-hover:text-blue-300 transition-colors">
            <span className="text-sm font-medium">Read full article</span>
            <span className="ml-1 group-hover:translate-x-1 transition-transform">→</span>
          </div>
        </div>
      </article>
    </Link>
  );
};

export default NewsCard;