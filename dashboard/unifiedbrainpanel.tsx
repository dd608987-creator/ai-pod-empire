import React, { useEffect, useState } from "react";

export default function UnifiedBrainPanel() {
  const [status, setStatus] = useState<any>(null);

  useEffect(() => {
    fetch("/empire/run", { method: "POST" })
      .then((res) => res.json())
      .then((data) => setStatus(data));
  }, []);

  if (!status) return <div>Loading AI Empire...</div>;

  return (
    <div style={{ padding: 20, fontFamily: "Arial" }}>
      <h1>🧠 Unified Brain — AI POD Empire</h1>

      <section>
        <h2>📈 Trends</h2>
        <pre>{JSON.stringify(status.trends, null, 2)}</pre>
      </section>

      <section>
        <h2>🎨 Designs</h2>
        <pre>{JSON.stringify(status.designs, null, 2)}</pre>
      </section>

      <section>
        <h2>🖼 Mockups</h2>
        <pre>{JSON.stringify(status.mockups, null, 2)}</pre>
      </section>

      <section>
        <h2>📦 Collections</h2>
        <pre>{JSON.stringify(status.collections, null, 2)}</pre>
      </section>

      <section>
        <h2>📚 Learning</h2>
        <pre>{JSON.stringify(status.learning, null, 2)}</pre>
      </section>

      <section>
        <h2>⚙️ Auto‑Scaling</h2>
        <pre>{JSON.stringify(status.scaling, null, 2)}</pre>
      </section>

      <section>
        <h2>💰 Revenue Optimization</h2>
        <pre>{JSON.stringify(status.revenue, null, 2)}</pre>
      </section>

      <section>
        <h2>🧬 Design Evolution</h2>
        <pre>{JSON.stringify(status.evolution, null, 2)}</pre>
      </section>
    </div>
  );
        }
