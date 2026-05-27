import React from "react";
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid } from "recharts";

const data = [
  { name: "TikTok", score: 92 },
  { name: "Instagram", score: 78 },
  { name: "YouTube", score: 85 }
];

export default function ChartCard() {
  return (
    <div className="bg-gray-800 p-4 rounded-xl shadow-lg">
      <h2 className="text-xl font-semibold mb-4">Platform Performance</h2>
      <LineChart width={400} height={250} data={data}>
        <CartesianGrid stroke="#444" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey="score" stroke="#00eaff" strokeWidth={3} />
      </LineChart>
    </div>
  );
}
