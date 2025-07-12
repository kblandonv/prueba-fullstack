import { useState } from "react";
import SearchForm from "./components/SearchForm.jsx";
import ArticleView from "./components/ArticleView.jsx";
import "./App.css";

function App() {
  const [article, setArticle] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSearch = async (topic) => {
    setLoading(true);
    try {
      const res = await fetch("http://localhost:8001/topics/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: topic }),
      });
      if (!res.ok) throw new Error("No se encontró contenido");
      const data = await res.json();
      setArticle(data);
    } catch (err) {
      alert(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div container>
      <div style={{ padding: "2rem" }}>
        <h1>Web Scraper App</h1>
        <SearchForm onSearch={handleSearch} />
        {loading && <p>Cargando…</p>}
        {article && <ArticleView article={article} />}
      </div>
    </div>
  );
}

export default App;
