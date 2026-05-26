import React, { useEffect, useState } from "react";
import { View, Text, ScrollView, StyleSheet } from "react-native";

export default function App() {
  const [status, setStatus] = useState<any>(null);

  useEffect(() => {
    fetch("https://your-api-url.com/empire/run", { method: "POST" })
      .then((res) => res.json())
      .then((data) => setStatus(data))
      .catch(() => setStatus({ error: "Unable to connect to AI Empire API" }));
  }, []);

  if (!status) {
    return (
      <View style={styles.container}>
        <Text style={styles.loading}>Loading AI Empire...</Text>
      </View>
    );
  }

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>🧠 AI POD Empire — Mobile Dashboard</Text>

      <Section title="📈 Trends" data={status.trends} />
      <Section title="🎨 Designs" data={status.designs} />
      <Section title="🖼 Mockups" data={status.mockups} />
      <Section title="📦 Collections" data={status.collections} />
      <Section title="📚 Learning" data={status.learning} />
      <Section title="⚙️ Auto‑Scaling" data={status.scaling} />
      <Section title="💰 Revenue Optimization" data={status.revenue} />
      <Section title="🧬 Design Evolution" data={status.evolution} />
    </ScrollView>
  );
}

function Section({ title, data }) {
  return (
    <View style={styles.section}>
      <Text style={styles.sectionTitle}>{title}</Text>
      <Text style={styles.code}>{JSON.stringify(data, null, 2)}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 20,
    marginTop: 40,
    backgroundColor: "#fff",
  },
  title: {
    fontSize: 22,
    fontWeight: "bold",
    marginBottom: 20,
  },
  section: {
    marginBottom: 25,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: "600",
    marginBottom: 10,
  },
  code: {
    fontFamily: "monospace",
    backgroundColor: "#f4f4f4",
    padding: 10,
    borderRadius: 8,
  },
  loading: {
    fontSize: 20,
    fontWeight: "bold",
  },
});
