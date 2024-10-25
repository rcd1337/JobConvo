
import {Navbar} from "@/ui/navbar";
import { BarChart, Bar, Rectangle, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import styles from '@/styles/Applications.module.css'
import {getJobListingData} from '@/actions/reports'
import React, { useState } from 'react'
import { useEffect } from 'react';

export default function Page() {

  const [barData, setBarData] = useState({});

  useEffect(() => {
    const reportData = getJobListingData();
    setBarData(reportData)
  }, [])

  console.log(barData)
  return (
    <>
      <Navbar/>
      <div className={styles.page}>
        <ResponsiveContainer className={styles.cardContainer}>
            <BarChart
            width={500}
            height={300}
            data={barData["applications_count_data"]}
            margin={{
                top: 5,
                right: 15,
                left: 15,
                bottom: 5,
            }}
            >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="applications" fill="#8884d8" activeBar={<Rectangle fill="pink" stroke="blue" />} />
            <Bar dataKey="job_listings" fill="#82ca9d" activeBar={<Rectangle fill="gold" stroke="purple" />} />
            </BarChart>
        </ResponsiveContainer>
        </div>
    </>
  );
}
