import React from "react";

export default function MetricCard({ title, value }) {
  return (
    <div className="bg-gray-800 p-4 rounded-xl shadow-lg">
      <h2 className="text-xl font-semibold">{title}</h2>
      <p className="text-3xl mt-2">{value}</p>
    </div>
  );
}
