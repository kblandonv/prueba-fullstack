import React, { useState } from 'react';

export default function SearchForm({ onSearch }) {
  const [topic, setTopic] = useState('');
  return (
    <form
      className="search-form"
      onSubmit={e => {
        e.preventDefault();
        onSearch(topic);
      }}
    >
      <input
        type="text"
        value={topic}
        onChange={e => setTopic(e.target.value)}
        placeholder="Ingresa un tema…"
      />
      <button type="submit">Buscar</button>
    </form>
  );
}
