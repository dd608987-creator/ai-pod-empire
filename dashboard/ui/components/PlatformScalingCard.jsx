import React from "react";

export default function PlatformScalingCard() {
  return (
    <div className="bg-gray-800 p-4 rounded-xl shadow-lg">
      <h2 className="text-xl font-semibold mb-4">Auto‑Scaling Strategy</h2>

      <p className="text-lg">Scale Up: <span className="text-green-400">TikTok</span></p>
      <p className="text-lg">Scale Down: <span className="text-red-400">Facebook Reels</span></p>
      <p className="text-lg">Recommended Frequency: 3 posts/day</p>
    </div>
  );
}
