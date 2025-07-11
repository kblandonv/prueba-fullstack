import React from 'react';

export default function ArticleView({ article }) {
  return (
    <div className="article">
      <h2>{article.name}</h2>
      <p>{article.content}</p>
    </div>
  );
}
