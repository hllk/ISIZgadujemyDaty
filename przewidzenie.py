# -*- coding: utf-8 -*-

"""Na podstawie ilosci i, y, j przewiduje jaki byl rok napisania tekstu."""

import re
import sys
import operator
import glob
import math

dane1 = [(1775, 245.00, 125.00, 6.00), 
(1776, 246.00, 139.00, 8.00), 
(1777, 0.00, 0.00, 0.00), 
(1778, 244.00, 148.00, 10.00), 
(1779, 251.00, 148.00, 10.00), 
(1780, 248.00, 146.00, 8.00), 
(1781, 238.00, 149.00, 8.00), 
(1782, 252.00, 152.00, 9.00), 
(1783, 244.00, 123.00, 22.00), 
(1784, 0.00, 0.00, 0.00), 
(1785, 240.00, 137.00, 23.00), 
(1786, 245.00, 140.00, 6.00), 
(1787, 254.00, 141.00, 10.00), 
(1788, 251.00, 151.00, 10.00), 
(1789, 235.00, 169.00, 13.00), 
(1790, 253.00, 151.00, 10.00), 
(1791, 258.00, 162.00, 11.00), 
(1792, 262.00, 146.00, 8.00), 
(1793, 253.00, 142.00, 8.00), 
(1794, 260.00, 143.00, 4.00), 
(1795, 268.00, 140.00, 3.00), 
(1796, 251.00, 110.00, 5.00), 
(1797, 0.00, 0.00, 0.00), 
(1798, 227.00, 69.00, 4.00), 
(1799, 251.00, 110.00, 4.00), 
(1800, 255.00, 125.00, 8.00), 
(1801, 263.00, 125.00, 7.00), 
(1802, 258.00, 103.00, 5.00), 
(1803, 257.00, 118.00, 7.00), 
(1804, 272.00, 125.00, 9.00), 
(1805, 268.00, 130.00, 5.00), 
(1806, 267.00, 120.00, 5.00), 
(1807, 272.00, 131.00, 6.00), 
(1808, 276.00, 139.00, 4.00), 
(1809, 274.00, 138.00, 5.00), 
(1810, 273.00, 138.00, 4.00), 
(1811, 265.00, 135.00, 4.00), 
(1812, 230.00, 107.00, 5.00), 
(1813, 269.00, 130.00, 4.00), 
(1814, 268.00, 133.00, 8.00), 
(1815, 267.00, 128.00, 8.00), 
(1816, 276.00, 134.00, 6.00), 
(1817, 266.00, 132.00, 4.00), 
(1818, 260.00, 126.00, 14.00), 
(1819, 256.00, 123.00, 11.00), 
(1820, 264.00, 129.00, 4.00), 
(1821, 263.00, 123.00, 15.00), 
(1822, 267.00, 119.00, 20.00), 
(1823, 267.00, 119.00, 20.00), 
(1824, 265.00, 119.00, 14.00), 
(1825, 262.00, 120.00, 13.00), 
(1826, 263.00, 117.00, 19.00), 
(1827, 249.00, 110.00, 36.00), 
(1828, 256.00, 114.00, 30.00), 
(1829, 247.00, 114.00, 34.00), 
(1830, 242.00, 111.00, 38.00), 
(1831, 251.00, 117.00, 34.00), 
(1832, 248.00, 111.00, 36.00), 
(1833, 244.00, 111.00, 39.00), 
(1834, 243.00, 108.00, 42.00), 
(1835, 236.00, 108.00, 49.00), 
(1836, 232.00, 103.00, 51.00), 
(1837, 230.00, 101.00, 51.00), 
(1838, 231.00, 102.00, 52.00), 
(1839, 234.00, 101.00, 51.00), 
(1840, 234.00, 102.00, 50.00), 
(1841, 232.00, 107.00, 59.00), 
(1842, 244.00, 105.00, 64.00), 
(1843, 239.00, 106.00, 62.00), 
(1844, 234.00, 106.00, 60.00), 
(1845, 232.00, 104.00, 59.00), 
(1846, 234.00, 106.00, 61.00), 
(1847, 233.00, 102.00, 59.00), 
(1848, 231.00, 103.00, 60.00), 
(1849, 227.00, 101.00, 59.00), 
(1850, 223.00, 101.00, 61.00), 
(1851, 223.00, 101.00, 63.00), 
(1852, 225.00, 102.00, 60.00), 
(1853, 221.00, 103.00, 57.00), 
(1854, 224.00, 103.00, 59.00), 
(1855, 224.00, 103.00, 59.00), 
(1856, 226.00, 105.00, 59.00), 
(1857, 224.00, 103.00, 58.00), 
(1858, 227.00, 104.00, 58.00), 
(1859, 225.00, 103.00, 60.00), 
(1860, 225.00, 102.00, 59.00), 
(1861, 225.00, 102.00, 58.00), 
(1862, 227.00, 99.00, 59.00), 
(1863, 226.00, 101.00, 60.00), 
(1864, 224.00, 102.00, 60.00), 
(1865, 220.00, 100.00, 57.00), 
(1866, 223.00, 100.00, 57.00), 
(1867, 217.00, 98.00, 55.00), 
(1868, 224.00, 100.00, 57.00), 
(1869, 222.00, 103.00, 57.00), 
(1870, 212.00, 97.00, 53.00), 
(1871, 213.00, 98.00, 55.00), 
(1872, 216.00, 102.00, 55.00), 
(1873, 210.00, 95.00, 55.00), 
(1874, 215.00, 99.00, 54.00), 
(1875, 212.00, 99.00, 52.00), 
(1876, 207.00, 95.00, 51.00), 
(1877, 213.00, 98.00, 55.00), 
(1878, 221.00, 103.00, 55.00), 
(1879, 220.00, 102.00, 54.00), 
(1880, 223.00, 103.00, 54.00), 
(1881, 219.00, 101.00, 54.00), 
(1882, 223.00, 101.00, 54.00), 
(1883, 218.00, 97.00, 55.00), 
(1884, 220.00, 98.00, 55.00), 
(1885, 211.00, 97.00, 53.00), 
(1886, 217.00, 101.00, 56.00), 
(1887, 218.00, 106.00, 49.00), 
(1888, 211.00, 104.00, 47.00), 
(1889, 212.00, 105.00, 49.00), 
(1890, 208.00, 102.00, 47.00), 
(1891, 192.00, 95.00, 46.00), 
(1892, 208.00, 102.00, 46.00), 
(1893, 212.00, 105.00, 48.00), 
(1894, 189.00, 89.00, 44.00), 
(1895, 193.00, 96.00, 44.00), 
(1896, 195.00, 94.00, 45.00), 
(1897, 199.00, 97.00, 47.00), 
(1898, 199.00, 92.00, 45.00), 
(1899, 192.00, 89.00, 46.00), 
(1900, 205.00, 96.00, 48.00), 
(1901, 203.00, 98.00, 48.00), 
(1902, 203.00, 95.00, 44.00), 
(1903, 201.00, 93.00, 46.00), 
(1904, 200.00, 93.00, 44.00), 
(1905, 194.00, 89.00, 42.00), 
(1906, 216.00, 100.00, 50.00), 
(1907, 220.00, 101.00, 51.00), 
(1908, 223.00, 102.00, 53.00), 
(1909, 219.00, 105.00, 50.00), 
(1910, 215.00, 99.00, 53.00), 
(1911, 224.00, 101.00, 54.00), 
(1912, 220.00, 104.00, 53.00), 
(1913, 216.00, 100.00, 53.00), 
(1914, 223.00, 104.00, 51.00), 
(1915, 227.00, 105.00, 52.00), 
(1916, 221.00, 104.00, 51.00), 
(1917, 227.00, 104.00, 59.00), 
(1918, 233.00, 107.00, 61.00), 
(1919, 223.00, 101.00, 53.00), 
(1920, 213.00, 94.00, 49.00), 
(1921, 202.00, 93.00, 46.00), 
(1922, 187.00, 84.00, 43.00), 
(1923, 180.00, 85.00, 44.00), 
(1924, 185.00, 86.00, 44.00), 
(1925, 185.00, 85.00, 48.00), 
(1926, 201.00, 90.00, 52.00), 
(1927, 191.00, 88.00, 50.00), 
(1928, 196.00, 93.00, 52.00), 
(1929, 197.00, 93.00, 52.00), 
(1930, 192.00, 91.00, 52.00), 
(1931, 194.00, 94.00, 53.00), 
(1932, 203.00, 97.00, 55.00), 
(1933, 203.00, 97.00, 55.00), 
(1934, 204.00, 95.00, 55.00), 
(1935, 206.00, 95.00, 54.00), 
(1936, 205.00, 96.00, 54.00), 
(1937, 218.00, 101.00, 53.00), 
(1938, 213.00, 101.00, 54.00), 
(1939, 215.00, 102.00, 55.00), 
(1940, 167.00, 46.00, 19.00), 
(1941, 177.00, 40.00, 19.00), 
(1942, 172.00, 49.00, 19.00), 
(1943, 203.00, 95.00, 57.00), 
(1944, 196.00, 83.00, 50.00), 
(1945, 187.00, 90.00, 49.00), 
(1946, 192.00, 94.00, 47.00), 
(1947, 214.00, 107.00, 57.00), 
(1948, 197.00, 102.00, 54.00), 
(1949, 195.00, 95.00, 53.00), 
(1950, 168.00, 94.00, 47.00), 
(1951, 179.00, 93.00, 52.00), 
(1952, 157.00, 96.00, 48.00), 
(1953, 150.00, 85.00, 40.00), 
(1954, 189.00, 89.00, 50.00), 
(1955, 204.00, 95.00, 52.00), 
(1956, 194.00, 96.00, 52.00), 
(1957, 187.00, 93.00, 52.00), 
(1958, 185.00, 92.00, 48.00), 
(1959, 185.00, 91.00, 50.00), 
(1960, 193.00, 95.00, 52.00), 
(1961, 192.00, 95.00, 53.00), 
(1962, 194.00, 96.00, 52.00), 
(1963, 184.00, 92.00, 49.00), 
(1964, 201.00, 98.00, 55.00), 
(1965, 197.00, 98.00, 53.00), 
(1966, 192.00, 92.00, 51.00), 
(1967, 191.00, 95.00, 52.00), 
(1968, 180.00, 91.00, 50.00), 
(1969, 191.00, 88.00, 49.00), 
(1970, 191.00, 90.00, 49.00), 
(1971, 185.00, 89.00, 51.00), 
(1972, 191.00, 89.00, 50.00), 
(1973, 189.00, 89.00, 49.00), 
(1974, 190.00, 87.00, 49.00), 
(1975, 192.00, 88.00, 50.00), 
(1976, 197.00, 90.00, 51.00), 
(1977, 193.00, 82.00, 49.00), 
(1978, 184.00, 80.00, 46.00), 
(1979, 183.00, 80.00, 46.00), 
(1980, 178.00, 71.00, 43.00), 
(1981, 153.00, 66.00, 43.00), 
(1982, 193.00, 87.00, 50.00), 
(1983, 191.00, 88.00, 47.00), 
(1984, 185.00, 85.00, 48.00), 
(1985, 186.00, 90.00, 51.00), 
(1986, 184.00, 85.00, 50.00), 
(1987, 167.00, 81.00, 47.00), 
(1988, 156.00, 79.00, 44.00), 
(1989, 157.00, 77.00, 46.00), 
(1990, 170.00, 82.00, 45.00), 
(1991, 191.00, 90.00, 47.00), 
(1992, 209.00, 100.00, 54.00), 
(1993, 209.00, 93.00, 51.00), 
(1994, 209.00, 98.00, 54.00), 
(1995, 207.00, 95.00, 52.00), 
(1996, 198.00, 91.00, 50.00), 
(1997, 215.00, 96.00, 51.00), 
(1998, 203.00, 87.00, 49.00), 
(1999, 205.00, 93.00, 51.00), 
(2000, 194.00, 91.00, 48.00), 
(2001, 212.00, 95.00, 52.00), 
(2002, 218.00, 93.00, 49.00), 
(2003, 223.00, 104.00, 56.00), 
(2004, 215.00, 97.00, 54.00), 
(2005, 212.00, 98.00, 53.00), 
(2006, 217.00, 101.00, 54.00), 
(2007, 211.00, 95.00, 52.00), 
(2008, 218.00, 101.00, 56.00), 
(2009, 215.00, 101.00, 55.00), 
(2010, 230.00, 105.00, 58.00), 
(2011, 235.00, 106.00, 58.00), 
(2012, 235.00, 109.00, 60.00), 
(2013, 253.00, 100.00, 59.00)]

dane5 = [(1775, 245.00, 125.00, 6.00), 
(1776, 246.00, 139.00, 8.00), 
(1777, 246.34, 142.77, 8.96), 
(1778, 246.82, 145.17, 9.05), 
(1779, 245.49, 147.71, 9.18), 
(1780, 246.72, 148.52, 9.14), 
(1781, 247.71, 147.95, 9.20), 
(1782, 246.57, 147.94, 8.92), 
(1783, 245.64, 148.61, 9.82), 
(1784, 249.48, 146.68, 10.00), 
(1785, 247.42, 137.25, 11.42), 
(1786, 249.47, 145.26, 9.63), 
(1787, 245.19, 152.30, 10.63), 
(1788, 247.18, 152.44, 10.12), 
(1789, 250.79, 156.88, 10.88), 
(1790, 255.99, 152.53, 9.55), 
(1791, 255.34, 148.81, 8.94), 
(1792, 257.95, 145.87, 7.23), 
(1793, 259.56, 144.80, 6.52), 
(1794, 259.52, 142.34, 6.05), 
(1795, 258.63, 141.03, 5.35), 
(1796, 258.44, 133.09, 3.76), 
(1797, 254.88, 117.08, 3.60), 
(1798, 251.12, 115.74, 6.75), 
(1799, 256.37, 119.98, 6.91), 
(1800, 256.67, 116.86, 6.56), 
(1801, 257.92, 119.05, 6.78), 
(1802, 261.30, 120.79, 7.40), 
(1803, 263.74, 121.34, 6.89), 
(1804, 264.66, 120.13, 6.43), 
(1805, 266.82, 124.18, 6.52), 
(1806, 271.14, 128.82, 5.87), 
(1807, 271.55, 131.62, 4.98), 
(1808, 272.43, 133.59, 4.71), 
(1809, 271.63, 136.35, 4.49), 
(1810, 257.45, 127.05, 4.47), 
(1811, 257.05, 126.00, 4.45), 
(1812, 257.55, 126.19, 5.18), 
(1813, 256.46, 124.45, 5.86), 
(1814, 258.69, 124.54, 6.17), 
(1815, 269.24, 131.57, 6.13), 
(1816, 267.20, 130.58, 8.24), 
(1817, 264.85, 128.53, 8.83), 
(1818, 264.27, 128.75, 7.58), 
(1819, 262.20, 126.04, 10.36), 
(1820, 263.67, 122.80, 14.63), 
(1821, 265.05, 121.31, 16.38), 
(1822, 265.61, 120.72, 16.22), 
(1823, 265.07, 119.78, 16.78), 
(1824, 264.97, 118.81, 17.45), 
(1825, 260.06, 116.28, 22.19), 
(1826, 257.72, 115.22, 24.32), 
(1827, 254.23, 114.36, 28.04), 
(1828, 249.69, 112.65, 32.89), 
(1829, 248.34, 113.05, 34.84), 
(1830, 248.12, 113.11, 34.92), 
(1831, 246.18, 112.52, 36.47), 
(1832, 245.31, 111.23, 38.12), 
(1833, 243.36, 110.39, 41.10), 
(1834, 239.77, 107.85, 44.28), 
(1835, 236.35, 105.86, 47.04), 
(1836, 234.38, 104.49, 49.02), 
(1837, 232.59, 103.38, 50.67), 
(1838, 231.81, 101.86, 51.05), 
(1839, 231.78, 102.19, 52.13), 
(1840, 234.43, 103.12, 54.47), 
(1841, 236.47, 104.09, 56.89), 
(1842, 236.46, 105.13, 58.76), 
(1843, 236.08, 105.59, 60.75), 
(1844, 236.37, 105.43, 61.11), 
(1845, 234.50, 104.88, 60.25), 
(1846, 232.60, 104.12, 59.84), 
(1847, 231.01, 103.04, 59.61), 
(1848, 229.47, 102.53, 59.95), 
(1849, 227.73, 101.71, 60.22), 
(1850, 226.48, 101.71, 60.37), 
(1851, 224.07, 101.56, 59.84), 
(1852, 223.19, 102.03, 59.91), 
(1853, 223.40, 102.45, 59.49), 
(1854, 224.01, 103.22, 58.79), 
(1855, 223.82, 103.41, 58.41), 
(1856, 225.02, 103.61, 58.60), 
(1857, 225.23, 103.62, 58.76), 
(1858, 225.44, 103.45, 58.76), 
(1859, 225.23, 102.81, 58.55), 
(1860, 225.91, 101.81, 58.77), 
(1861, 225.72, 101.20, 59.19), 
(1862, 225.54, 101.05, 59.20), 
(1863, 224.75, 100.72, 58.89), 
(1864, 224.42, 100.35, 58.77), 
(1865, 222.20, 100.24, 57.94), 
(1866, 221.45, 99.98, 57.20), 
(1867, 220.97, 100.09, 56.53), 
(1868, 219.10, 99.40, 55.63), 
(1869, 216.96, 98.96, 55.23), 
(1870, 216.73, 99.87, 55.23), 
(1871, 214.48, 99.05, 54.91), 
(1872, 213.43, 98.43, 54.39), 
(1873, 213.39, 98.83, 54.13), 
(1874, 212.00, 98.12, 53.23), 
(1875, 211.32, 97.27, 53.17), 
(1876, 213.04, 98.51, 53.18), 
(1877, 213.83, 99.01, 53.15), 
(1878, 215.88, 99.71, 53.58), 
(1879, 219.05, 101.32, 54.40), 
(1880, 221.23, 101.92, 54.18), 
(1881, 220.44, 100.47, 54.26), 
(1882, 220.39, 99.58, 54.49), 
(1883, 217.85, 98.53, 54.21), 
(1884, 217.51, 98.71, 54.62), 
(1885, 216.63, 99.17, 54.07), 
(1886, 215.61, 100.27, 52.96), 
(1887, 213.83, 101.61, 51.80), 
(1888, 213.80, 103.20, 50.60), 
(1889, 210.02, 103.23, 47.78), 
(1890, 207.80, 102.34, 47.10), 
(1891, 208.09, 102.60, 47.33), 
(1892, 204.33, 100.02, 46.44), 
(1893, 201.46, 98.83, 45.88), 
(1894, 201.90, 98.75, 45.76), 
(1895, 199.51, 97.44, 45.88), 
(1896, 195.05, 93.44, 44.92), 
(1897, 195.59, 93.35, 45.34), 
(1898, 198.34, 93.41, 46.25), 
(1899, 199.67, 94.20, 46.75), 
(1900, 200.49, 93.96, 46.12), 
(1901, 200.92, 94.13, 46.32), 
(1902, 202.17, 94.70, 45.80), 
(1903, 199.90, 93.23, 44.59), 
(1904, 205.29, 95.11, 46.14), 
(1905, 210.05, 96.93, 47.86), 
(1906, 214.61, 98.76, 49.48), 
(1907, 217.17, 100.84, 50.17), 
(1908, 218.69, 101.48, 51.42), 
(1909, 220.17, 101.65, 52.17), 
(1910, 220.17, 102.22, 52.55), 
(1911, 218.93, 101.95, 52.51), 
(1912, 219.39, 101.39, 53.00), 
(1913, 221.87, 102.65, 52.83), 
(1914, 221.10, 103.36, 52.19), 
(1915, 222.98, 103.33, 53.72), 
(1916, 226.65, 104.84, 55.44), 
(1917, 226.55, 104.29, 55.69), 
(1918, 224.33, 102.53, 55.37), 
(1919, 221.11, 100.65, 54.53), 
(1920, 211.56, 95.86, 50.61), 
(1921, 199.31, 90.78, 46.69), 
(1922, 191.25, 87.69, 44.86), 
(1923, 186.93, 86.24, 44.98), 
(1924, 187.92, 86.14, 46.35), 
(1925, 188.84, 86.94, 47.80), 
(1926, 191.77, 88.61, 49.32), 
(1927, 194.30, 90.17, 50.95), 
(1928, 195.12, 91.10, 51.61), 
(1929, 194.03, 91.85, 51.83), 
(1930, 196.43, 93.61, 52.82), 
(1931, 197.97, 94.47, 53.44), 
(1932, 199.59, 94.87, 54.08), 
(1933, 202.27, 95.60, 54.45), 
(1934, 204.23, 95.96, 54.59), 
(1935, 206.98, 96.71, 54.23), 
(1936, 208.99, 97.54, 54.03), 
(1937, 211.00, 98.76, 53.94), 
(1938, 211.95, 99.33, 53.66), 
(1939, 214.39, 100.09, 53.20), 
(1940, 212.32, 99.41, 53.17), 
(1941, 211.04, 96.94, 52.06), 
(1942, 193.85, 79.55, 47.18), 
(1943, 193.41, 83.03, 48.63), 
(1944, 193.84, 85.27, 49.48), 
(1945, 197.18, 88.97, 50.90), 
(1946, 197.03, 90.86, 51.25), 
(1947, 196.87, 97.34, 52.71), 
(1948, 196.13, 98.51, 52.92), 
(1949, 193.74, 97.96, 53.19), 
(1950, 187.49, 96.12, 52.12), 
(1951, 180.84, 93.41, 50.27), 
(1952, 174.86, 90.77, 48.43), 
(1953, 185.38, 91.84, 49.78), 
(1954, 188.88, 92.80, 50.02), 
(1955, 190.21, 92.67, 50.55), 
(1956, 193.25, 93.27, 51.26), 
(1957, 192.30, 93.67, 51.25), 
(1958, 189.47, 93.65, 51.23), 
(1959, 189.03, 93.43, 51.49), 
(1960, 190.36, 93.98, 51.46), 
(1961, 190.04, 93.90, 51.44), 
(1962, 194.08, 95.63, 52.71), 
(1963, 194.66, 96.04, 52.92), 
(1964, 194.61, 95.17, 52.35), 
(1965, 194.30, 94.98, 52.38), 
(1966, 194.23, 94.98, 52.60), 
(1967, 190.84, 91.59, 50.57), 
(1968, 190.33, 90.54, 49.89), 
(1969, 188.48, 89.76, 49.91), 
(1970, 188.88, 89.16, 49.76), 
(1971, 189.44, 89.01, 49.59), 
(1972, 189.25, 88.81, 49.59), 
(1973, 189.47, 88.40, 49.79), 
(1974, 191.75, 88.59, 49.79), 
(1975, 192.18, 87.06, 49.58), 
(1976, 191.07, 85.21, 48.94), 
(1977, 189.65, 83.82, 48.34), 
(1978, 186.81, 80.39, 46.92), 
(1979, 175.49, 74.74, 45.15), 
(1980, 174.20, 74.82, 44.99), 
(1981, 175.39, 76.24, 45.17), 
(1982, 174.86, 76.41, 45.30), 
(1983, 175.36, 79.22, 46.49), 
(1984, 188.67, 87.18, 48.86), 
(1985, 183.76, 86.10, 48.26), 
(1986, 174.70, 83.76, 47.79), 
(1987, 168.80, 82.06, 47.37), 
(1988, 165.57, 80.48, 46.29), 
(1989, 166.98, 81.41, 45.78), 
(1990, 173.79, 84.52, 46.83), 
(1991, 185.02, 87.56, 48.36), 
(1992, 197.97, 92.76, 50.26), 
(1993, 204.92, 95.11, 51.58), 
(1994, 205.88, 95.09, 52.06), 
(1995, 207.16, 94.52, 51.56), 
(1996, 206.14, 93.41, 51.19), 
(1997, 205.41, 92.51, 50.65), 
(1998, 203.16, 91.66, 49.89), 
(1999, 205.97, 92.37, 50.21), 
(2000, 206.20, 91.66, 49.79), 
(2001, 210.12, 95.06, 51.15), 
(2002, 212.80, 96.13, 52.09), 
(2003, 215.39, 97.43, 52.96), 
(2004, 216.26, 98.82, 53.40), 
(2005, 214.61, 98.34, 53.45), 
(2006, 214.75, 98.52, 53.86), 
(2007, 214.77, 99.25, 54.07), 
(2008, 217.68, 100.38, 54.88), 
(2009, 220.11, 100.99, 55.48), 
(2010, 224.62, 103.69, 57.03), 
(2011, 227.45, 104.57, 57.42), 
(2012, 235.00, 109.00, 60.00), 
(2013, 253.00, 100.00, 59.00)]

dane17 = [(1775, 245.00, 125.00, 6.00), 
(1776, 246.00, 139.00, 8.00), 
(1777, 0.00, 0.00, 0.00), 
(1778, 244.00, 148.00, 10.00), 
(1779, 251.00, 148.00, 10.00), 
(1780, 248.00, 146.00, 8.00), 
(1781, 238.00, 149.00, 8.00), 
(1782, 252.00, 152.00, 9.00), 
(1783, 247.43, 147.63, 22.00), 
(1784, 250.12, 148.26, 0.00), 
(1785, 251.05, 148.13, 23.00), 
(1786, 252.44, 147.33, 6.00), 
(1787, 254.55, 146.69, 10.00), 
(1788, 254.77, 146.11, 10.00), 
(1789, 255.31, 146.12, 13.00), 
(1790, 255.43, 143.33, 10.00), 
(1791, 255.48, 140.78, 11.00), 
(1792, 255.49, 138.07, 8.00), 
(1793, 256.75, 135.87, 8.00), 
(1794, 256.90, 133.27, 4.00), 
(1795, 257.08, 131.06, 3.00), 
(1796, 258.81, 130.27, 5.00), 
(1797, 259.67, 129.81, 0.00), 
(1798, 260.81, 128.18, 4.00), 
(1799, 261.84, 128.04, 4.00), 
(1800, 263.12, 128.12, 8.00), 
(1801, 264.07, 127.74, 7.00), 
(1802, 265.83, 127.99, 5.00), 
(1803, 266.13, 127.71, 7.00), 
(1804, 260.23, 124.01, 9.00), 
(1805, 260.98, 124.55, 5.00), 
(1806, 261.70, 125.42, 5.00), 
(1807, 262.37, 126.06, 6.00), 
(1808, 263.53, 126.85, 4.00), 
(1809, 264.10, 127.30, 5.00), 
(1810, 263.81, 127.30, 4.00), 
(1811, 263.44, 127.61, 4.00), 
(1812, 263.79, 128.20, 5.00), 
(1813, 263.37, 127.58, 4.00), 
(1814, 263.94, 125.94, 8.00), 
(1815, 264.38, 124.92, 8.00), 
(1816, 264.29, 124.09, 6.00), 
(1817, 263.79, 123.32, 4.00), 
(1818, 263.51, 122.38, 14.00), 
(1819, 261.11, 120.14, 11.00), 
(1820, 260.50, 119.19, 4.00), 
(1821, 260.17, 119.08, 15.00), 
(1822, 257.41, 117.73, 20.00), 
(1823, 256.48, 117.32, 20.00), 
(1824, 255.28, 116.38, 14.00), 
(1825, 253.75, 115.53, 13.00), 
(1826, 252.32, 114.43, 19.00), 
(1827, 250.09, 113.43, 36.00), 
(1828, 248.07, 112.20, 30.00), 
(1829, 245.98, 110.80, 34.00), 
(1830, 244.57, 109.92, 38.00), 
(1831, 243.29, 109.18, 34.00), 
(1832, 241.94, 108.47, 36.00), 
(1833, 240.88, 108.10, 39.00), 
(1834, 240.39, 107.64, 42.00), 
(1835, 239.66, 107.29, 49.00), 
(1836, 238.95, 107.10, 51.00), 
(1837, 238.03, 106.71, 51.00), 
(1838, 237.49, 106.39, 52.00), 
(1839, 237.03, 105.92, 51.00), 
(1840, 235.89, 105.15, 50.00), 
(1841, 234.53, 104.51, 59.00), 
(1842, 233.39, 103.93, 64.00), 
(1843, 232.18, 103.47, 62.00), 
(1844, 231.43, 102.91, 60.00), 
(1845, 230.82, 102.91, 59.00), 
(1846, 230.52, 103.13, 61.00), 
(1847, 230.10, 103.22, 59.00), 
(1848, 229.64, 103.45, 60.00), 
(1849, 229.05, 103.51, 59.00), 
(1850, 228.79, 103.37, 61.00), 
(1851, 227.90, 103.28, 63.00), 
(1852, 227.08, 103.04, 60.00), 
(1853, 226.56, 102.81, 57.00), 
(1854, 226.30, 102.46, 59.00), 
(1855, 225.86, 102.17, 59.00), 
(1856, 225.42, 102.17, 59.00), 
(1857, 224.65, 101.99, 58.00), 
(1858, 224.38, 101.97, 58.00), 
(1859, 224.03, 101.80, 60.00), 
(1860, 224.08, 101.76, 59.00), 
(1861, 223.93, 101.80, 58.00), 
(1862, 223.38, 101.44, 59.00), 
(1863, 222.67, 101.13, 60.00), 
(1864, 222.15, 101.07, 60.00), 
(1865, 221.35, 100.55, 57.00), 
(1866, 220.77, 100.30, 57.00), 
(1867, 219.78, 99.98, 55.00), 
(1868, 218.60, 99.47, 57.00), 
(1869, 217.96, 99.25, 57.00), 
(1870, 217.66, 99.26, 53.00), 
(1871, 217.03, 99.43, 55.00), 
(1872, 216.65, 99.49, 55.00), 
(1873, 216.34, 99.43, 55.00), 
(1874, 216.59, 99.50, 54.00), 
(1875, 216.37, 99.28, 52.00), 
(1876, 216.64, 99.25, 51.00), 
(1877, 215.88, 99.04, 55.00), 
(1878, 215.70, 99.02, 55.00), 
(1879, 216.00, 99.41, 54.00), 
(1880, 215.97, 99.69, 54.00), 
(1881, 215.80, 99.76, 54.00), 
(1882, 215.74, 100.07, 54.00), 
(1883, 215.27, 100.03, 55.00), 
(1884, 215.15, 100.20, 55.00), 
(1885, 215.63, 100.84, 53.00), 
(1886, 214.98, 100.66, 56.00), 
(1887, 213.92, 100.37, 49.00), 
(1888, 213.11, 100.13, 47.00), 
(1889, 212.15, 99.87, 49.00), 
(1890, 211.14, 99.47, 47.00), 
(1891, 209.44, 98.94, 46.00), 
(1892, 208.36, 99.00, 46.00), 
(1893, 206.70, 99.09, 48.00), 
(1894, 205.92, 99.15, 44.00), 
(1895, 204.01, 98.45, 44.00), 
(1896, 202.69, 97.49, 45.00), 
(1897, 201.46, 96.41, 47.00), 
(1898, 202.79, 96.33, 45.00), 
(1899, 204.87, 96.63, 46.00), 
(1900, 207.65, 97.40, 48.00), 
(1901, 209.06, 98.09, 48.00), 
(1902, 209.56, 97.83, 44.00), 
(1903, 211.57, 98.39, 46.00), 
(1904, 212.89, 98.97, 44.00), 
(1905, 213.42, 99.13, 42.00), 
(1906, 214.15, 99.39, 50.00), 
(1907, 215.31, 99.92, 51.00), 
(1908, 216.20, 100.40, 53.00), 
(1909, 217.24, 100.76, 50.00), 
(1910, 218.42, 101.16, 53.00), 
(1911, 219.06, 101.33, 54.00), 
(1912, 219.44, 101.33, 53.00), 
(1913, 219.44, 101.30, 53.00), 
(1914, 218.61, 100.82, 51.00), 
(1915, 216.76, 100.04, 52.00), 
(1916, 214.29, 98.98, 51.00), 
(1917, 211.71, 97.85, 59.00), 
(1918, 210.33, 96.68, 61.00), 
(1919, 208.26, 95.73, 53.00), 
(1920, 205.98, 95.08, 49.00), 
(1921, 204.03, 94.20, 46.00), 
(1922, 202.29, 93.60, 43.00), 
(1923, 200.86, 93.27, 44.00), 
(1924, 199.92, 93.08, 44.00), 
(1925, 199.46, 93.05, 48.00), 
(1926, 198.49, 92.68, 52.00), 
(1927, 197.71, 92.29, 50.00), 
(1928, 197.52, 92.33, 52.00), 
(1929, 198.57, 92.90, 52.00), 
(1930, 199.60, 93.53, 52.00), 
(1931, 200.75, 94.25, 53.00), 
(1932, 201.42, 94.48, 55.00), 
(1933, 202.18, 94.79, 55.00), 
(1934, 202.93, 95.20, 55.00), 
(1935, 203.02, 95.46, 54.00), 
(1936, 203.48, 95.37, 54.00), 
(1937, 203.75, 95.45, 53.00), 
(1938, 204.27, 95.66, 54.00), 
(1939, 205.54, 96.26, 55.00), 
(1940, 206.46, 96.58, 19.00), 
(1941, 206.36, 96.47, 19.00), 
(1942, 206.42, 96.37, 19.00), 
(1943, 206.27, 96.54, 57.00), 
(1944, 205.86, 96.80, 50.00), 
(1945, 205.09, 96.79, 49.00), 
(1946, 201.01, 95.33, 47.00), 
(1947, 196.81, 93.20, 57.00), 
(1948, 191.77, 91.12, 54.00), 
(1949, 191.67, 91.74, 53.00), 
(1950, 191.64, 92.25, 47.00), 
(1951, 191.21, 92.27, 52.00), 
(1952, 191.25, 92.44, 48.00), 
(1953, 190.39, 94.47, 40.00), 
(1954, 190.79, 94.81, 50.00), 
(1955, 190.51, 94.73, 52.00), 
(1956, 190.27, 94.40, 52.00), 
(1957, 190.08, 94.07, 52.00), 
(1958, 189.64, 93.78, 48.00), 
(1959, 190.27, 93.81, 50.00), 
(1960, 190.52, 93.77, 52.00), 
(1961, 191.14, 93.23, 53.00), 
(1962, 192.17, 93.15, 52.00), 
(1963, 191.79, 93.08, 49.00), 
(1964, 190.83, 92.59, 55.00), 
(1965, 190.47, 92.06, 53.00), 
(1966, 190.64, 91.60, 51.00), 
(1967, 190.86, 91.31, 52.00), 
(1968, 191.64, 91.23, 50.00), 
(1969, 191.67, 90.25, 49.00), 
(1970, 191.05, 89.16, 49.00), 
(1971, 190.34, 88.22, 51.00), 
(1972, 189.62, 86.88, 50.00), 
(1973, 184.88, 83.90, 49.00), 
(1974, 184.99, 83.76, 49.00), 
(1975, 184.99, 83.58, 50.00), 
(1976, 184.87, 83.39, 51.00), 
(1977, 184.99, 83.46, 49.00), 
(1978, 184.61, 83.24, 46.00), 
(1979, 183.58, 82.73, 46.00), 
(1980, 182.43, 82.20, 43.00), 
(1981, 180.88, 81.54, 43.00), 
(1982, 180.03, 81.03, 50.00), 
(1983, 179.68, 80.91, 47.00), 
(1984, 179.58, 80.91, 48.00), 
(1985, 179.21, 80.62, 51.00), 
(1986, 179.11, 81.18, 50.00), 
(1987, 180.10, 82.01, 47.00), 
(1988, 180.78, 82.67, 44.00), 
(1989, 182.67, 84.50, 46.00), 
(1990, 189.33, 88.14, 45.00), 
(1991, 189.92, 88.50, 47.00), 
(1992, 189.98, 88.68, 54.00), 
(1993, 191.29, 89.20, 51.00), 
(1994, 192.98, 89.35, 54.00), 
(1995, 194.93, 90.30, 52.00), 
(1996, 198.62, 91.53, 50.00), 
(1997, 202.86, 93.00, 51.00), 
(1998, 207.49, 94.99, 49.00), 
(1999, 209.41, 95.51, 51.00), 
(2000, 211.20, 96.37, 48.00), 
(2001, 211.65, 96.70, 52.00), 
(2002, 213.16, 97.47, 49.00), 
(2003, 214.54, 97.92, 56.00), 
(2004, 216.05, 98.68, 54.00), 
(2005, 217.19, 99.09, 53.00), 
(2006, 217.00, 101.00, 54.00), 
(2007, 211.00, 95.00, 52.00), 
(2008, 218.00, 101.00, 56.00), 
(2009, 215.00, 101.00, 55.00), 
(2010, 230.00, 105.00, 58.00), 
(2011, 235.00, 106.00, 58.00), 
(2012, 235.00, 109.00, 60.00), 
(2013, 253.00, 100.00, 59.00),]

def norma(a):
    return math.sqrt(a[0]*a[0]+a[1]*a[1]+a[2]*a[2])

def odleglosc(a, b):
    return float(a[1]*b[1]+a[2]*b[2]+a[0]*b[0])/float(norma(a)*norma(b))

def przewidzenie (ilei, iley, ilej):
    maxsuma = -1
    najblizszy = 1934 #najczestszy
    for aaa in dane17:
        (rok, i, y, j) = aaa
        if norma([i, y, j])!=0 and norma([ilei, iley, ilej])!=0 :
            if (odleglosc([ilei, iley, ilej], [i, y, j]) > maxsuma):
                maxsuma = odleglosc([ilei, iley, ilej], [i, y, j])
                najblizszy = rok
            #print odleglosc([ilei, iley, ilej], [i, y, j])
    #return 1934         #najczestszy
    return najblizszy

