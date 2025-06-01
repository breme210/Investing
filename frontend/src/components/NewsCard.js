import React from 'react';
import { Link } from 'react-router-dom';

const NewsCard = ({ article }) => {
  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  };

  const getCategoryColor = (category) => {
    const colors = {
      'Technology': 'bg-blue-600',
      'Product Updates': 'bg-green-600',
      'Industry News': 'bg-purple-600',
      'Company News': 'bg-orange-600'
    };
    return colors[category] || 'bg-gray-600';
  };

  // Get appropriate image based on category
  const getImageForCategory = (category) => {
    const images = {
      'Technology': 'https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
      'Product Updates': 'https://images.unsplash.com/photo-1531297484001-80022131f5a1?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
      'Industry News': 'https://images.unsplash.com/photo-1504711434969-e33886168f5c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
      'Company News': 'https://images.pexels.com/photos/7054384/pexels-photo-7054384.jpeg?auto=compress&cs=tinysrgb&w=800'
    };
    return images[category] || images['Technology'];
  };

  return (
    <Link to={`/news/${article.id}`} className="block group">
      <article className="bg-gray-800 rounded-lg overflow-hidden shadow-lg hover:shadow-xl transition-all duration-300 transform hover:scale-105">
        <div className="aspect-w-16 aspect-h-9">
          <img
            src={article.image_url || getImageForCategory(article.category)}
            alt={article.title}
            className="w-full h-48 object-cover group-hover:opacity-90 transition-opacity duration-300"
          />
        </div>
        
        <div className="p-6">
          <div className="flex items-center justify-between mb-3">
            <span className={`px-3 py-1 rounded-full text-xs font-medium text-white ${getCategoryColor(article.category)}`}>
              {article.category}
            </span>
            <span className="text-gray-400 text-sm">{article.read_time} min read</span>
          </div>
          
          <h3 className="text-xl font-semibold text-white mb-3 group-hover:text-blue-400 transition-colors duration-200 line-clamp-2">
            {article.title}
          </h3>
          
          <p className="text-gray-400 mb-4 line-clamp-3">
            {article.summary}
          </p>
          
          <div className="flex items-center justify-between">
            <span className="text-gray-500 text-sm">By {article.author}</span>
            <span className="text-gray-500 text-sm">{formatDate(article.publish_date)}</span>
          </div>
          
          {article.tags.length > 0 && (
            <div className="mt-4 flex flex-wrap gap-2">
              {article.tags.slice(0, 3).map((tag, index) => (
                <span
                  key={index}
                  className="px-2 py-1 bg-gray-700 text-gray-300 text-xs rounded"
                >
                  {tag}
                </span>
              ))}
            </div>
          )}
        </div>
      </article>
    </Link>
  );
};

export default NewsCard;